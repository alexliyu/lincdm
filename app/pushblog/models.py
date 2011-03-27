# -*- coding: utf-8 -*-
#  Copyright Š 2010 alexliyu email:alexliyu2012@gmail.com
# This file is part of CDM SYSTEM.
#
# CDM SYSTEM is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 0.3 of the License, or (at your option) any later
# version. WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# CDM SYSTEM. If not, see <http://www.gnu.org/licenses/>.
#  Copyright Š 2010 alexliyu email:alexliyu2012@gmail.com
from base import *
from datetime import datetime, timedelta
from lincdm.lib import htmllib
from app.htmllib import HTMLStripper
from lincdm.lib.gbtools import stringQ2B
from django.db import models
from datetime import datetime
import hashlib
import base64
import re
import htmlentitydefs
import time
import urllib, urllib2, Cookie, random
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class PushsList(models.Model):
		author_name = models.CharField()
		title = models.CharField(multiline=False, default='')
		date = models.DateTimeField(auto_now_add=True)
		tags = models.CharField()
		categorie_keys = models.ForeignKey()
		link = models.CharField(multiline=False, default='')
		excerpt = models.TextField()
		feed_link = models.CharField(multiline=False, default='')
		abconf = models.CharField(multiline=False, default='0')
		start_target = models.CharField(multiline=False, default='nohtml')
		mid_target = models.CharField(multiline=False, default='nohtml')
		end_target = models.CharField(multiline=False, default='nohtml')
		fetch_stat = models.IntegerField(default=0)
		content = models.TextField()

class PushList(models.Model):
		name = models.CharField(multiline=False, default='alexliyu')
		pushurl = models.CharField(multiline=False, default='http://blog.163.com/common/targetgo.s')
		username = models.CharField(multiline=False, default='alexliyu')
		password = models.CharField(multiline=False, default='password')
		latest = models.DateTimeField()
		last_retrieved = models.DateTimeField(default=datetime.today().fromtimestamp(0))
		acategory = models.CharField()
		category = models.CharField()
		pushnum = models.IntegerField(default=0)
		pushtime = models.IntegerField(default=0)

class PushSet(models.Model):
		defDate = models.IntegerField(default=3600)
		defStat = models.BooleanField(default=True)
		defDir = models.CharField(default='')
		last_checked = models.DateTimeField(default=datetime.today().fromtimestamp(0))
		stat = models.BooleanField(default=False)
		delitems = models.IntegerField(default=0)
		delitemi = models.IntegerField(default=0)
		chnitemi = models.IntegerField(default=0)
		entryerrs = models.IntegerField(default=0)
		entryerri = models.IntegerField(default=0)
		last_entry = models.IntegerField(default=0)
		last_feedslist = models.IntegerField(default=0)
		check_db_num = models.IntegerField(default=50)
		fetch_db_num = models.IntegerField(default=50)
		imgchecked_num = models.IntegerField(default=0)

class PushMethod():
		def Get_name(self, key=None):
				method = dict((['blog.163.com', 'Get_blog163'],
						['qzone.qq.com', 'Get_qzone'],
						['t.sina.com.cn', 'Get_sina_msgs'],
						['t.qq.com', 'Get_qq_msgs'],
						['qzone2.qq.com', 'Get_qzone2'],
						['t.163.com', 'Get_163_msgs'],
						['t.baidu.com', 'Get_baidu_msgs']
				))
				if key:
						return method[str(key)]
				else:
						return method

		def Get_Method(self, key, **kwargs):
				method = self.Get_name(key)
				result = self.Do_Method(method, **kwargs)
				return result

		def Do_Method(self, method, **kwargs):
				result = getattr(self, method)(**kwargs)
				return result



		def Get_blog163(self, model, pushitem, **kwargs):
			try:

				form_fields = {
						"title": htmllib.encoding(model.title, 'gb18030'),
						"content":htmllib.encoding(model.content, 'gb18030'),
						"name": pushitem.username,
						"password":pushitem.password
						}
				form_data = urllib.urlencode(form_fields)
				url = 'http://blog.163.com/common/targetgo.s'
				headers = {'Content-Type': 'application/x-www-form-urlencoded'}
				req = urllib2.Request(url, form_data, headers)
				result = urllib2.urlopen(req)

				if result.status_code == 200:
						return self.Get_True(model, pushitem)



				elif result.status_code == 500:
						logging.error('Push %s returned with status code 500.' % pushitem.pushurl)
						return self.Get_False(model, pushitem)
				elif result.status_code == 404:
						logging.error('Error 404: Nothing found at %s.' % pushitem.pushurl)
						return self.Get_False(model, pushitem)


			except Exception, data:
				return self.Get_False(model, pushitem, data)
				#break
				#logging.info('the error is %s',data)


		def Get_True(self, model, pushitem):
				"""
				if the result is True,we will do something to save db,
				and return the True
				"""
				pushitem.last_retrieved = datetime.now()
				pushitem.latest = model.date
				pushitem.put()
				return True

		def Get_False(self, model, pushitem, data=None):
				"""
				if the result is False,we will do something to save the result,and
				return the False
				"""
				logging.error('Could not push article %s ,and the push is restart now' % model.title)
				pushitem.last_retrieved = datetime.now()
				pushitem.latest = model.date
				if data:
						logging.info(data)
				pushitem.put()
				return False

		def Get_qzone(self, model, pushitem, **kwargs):
				try:
						message = mail.EmailMessage()
						message.sender = '%s@qq.com' % pushitem.username
						message.to = '%s@qzone.qq.com' % pushitem.username
						message.body = htmllib.encoding(stringQ2B(htmllib.encoding(model.content)), 'gb18030')
						message.subject = htmllib.encoding(stringQ2B(htmllib.encoding(model.title)), 'gb18030')
						message.send()
						return self.Get_True(model, pushitem)
				except Exception, data:
						return self.Get_False(model, pushitem, data)

		def Get_sina_msgs(self, model, pushitem, **kwargs):
				"""
				this method is used to get login to website,and put the content to the micro blog
				"""
				return self.Get_msgs(model, pushitem, 'send_sina_msgs', **kwargs)


		def Get_163_msgs(self, model, pushitem, **kwargs):
				return self.Get_msgs(model, pushitem, 'send_163_msgs', **kwargs)


		def Get_qq_msgs(self, model, pushitem, **kwargs):
				"""
				this method is used to get login to website,and put the content to the micro blog
				"""
				return self.Get_msgs(model, pushitem, 'send_qq_msgs', **kwargs)

		def Get_baidu_msgs(self, model, pushitem, **kwargs):
				"""
				this method is used to get login to website,and put the content to the micro blog
				"""
				return self.Get_msgs(model, pushitem, 'send_baidu_msgs', **kwargs)

		def Get_msgs(self, model, pushitem, method, **kwargs):
				"""
				this method is used to get login to website,and put the content to the micro blog
				"""
				try:



					content = '#%s# %s 详细内容请查看：%s' % (htmllib.encoding(model.title, 'utf-8'),
								htmllib.encoding(htmllib.Filter_html(model.excerpt)[:70], 'utf-8'),
								htmllib.encoding(model.fullurl, 'utf-8'))
					#content=htmllib.encoding(content,'utf-8')
					memcachekey = method
					result = getattr(self, method)(pushitem.username, pushitem.password, content, memcachekey)
					if result:
						return self.Get_True(model, pushitem)
					else:
						return self.Get_False(model, pushitem)
				except Exception, data:
						return self.Get_False(model, pushitem, data)




		def make_cookie_header(self, cookie):
				ret = ""
				for val in cookie.values():
						ret += "%s=%s; " % (val.key, val.value)
				return ret

		def Make_dict(self, content):
				"""
				the content is a dict,but fetch.response is string,so
				we must change the string to dict
				"""
				tmpval = dict()
				content = content[1:][:-1].replace('"', '')
				for val in content.split(','):
						tmpval.update({val.split(':')[0]:val.split(':')[1]})
				return tmpval

		def send_sina_msgs(self, username, password, msg, memcachekey):
			"""
			send sina msgs. use sina username, password.
			the msgs parameter is a message list, not a single string.
			"""
			try:
				result = urllib2.urlopen(url="https://login.sina.com.cn/sso/login.php?username=%s&password=%s&returntype=TEXT" % (username, password))
			except:
				return False
			if result.status_code == 200:
						tmpvalue = self.Make_dict(result.content)
						if not int(tmpvalue['retcode']) == 0:
								return False
			else:
						return False
			cookie = Cookie.SimpleCookie(result.headers.get('set-cookie', ''))
			msg = unescape(msg)
			form_fields = {
			  "content": msg,
			}
			form_data = urllib.urlencode(form_fields)
			url = 'http://t.sina.com.cn/mblog/publish.php?rnd=0.5100760071072727'
			headers = {'Referer':'http://t.sina.com.cn', 'Cookie' : self.make_cookie_header(cookie)}
			try:
				req = urllib2.Request(url, form_data, headers)
				result = urllib2.urlopen(req)
			except:
						return False
			if result.status_code == 200:
						return True
			else:
						return False

		def send_163_msgs(self, username, password, msg, memcachekey):
				"""
				send sina msgs. use sina username, password.
				the msgs parameter is a message list, not a single string.
				"""
				cookie = ''
				if memcache.get(memcachekey):
						cookie = memcache.get(memcachekey)
				else:
						try:
								result = urllib2.urlopen(url="https://reg.163.com/logins.jsp?username=%s&password=%s&product=t&type=1" % (username, password))
						except:
								return False
						if result.status_code == 200:
							pass
						else:
							return False
						cookie = Cookie.SimpleCookie(result.headers.get('set-cookie', ''))
						memcache.set(memcachekey, cookie, 36000)
				msg = unescape(msg)
				form_fields = {
				  "status": msg,
				}
				form_data = urllib.urlencode(form_fields)
				url = 'http://t.163.com/statuses/update.do'
				headers = {'Referer':'http://t.163.com', 'Cookie' : self.make_cookie_header(cookie)}
				
				try:
					req = urllib2.Request(url, form_data, headers)
					result = urllib2.urlopen(req)
				except Exception, data:
							logging.info(data)
							return False
				if result.status_code == 200:
							return True
				else:
							return False

		def send_baidu_msgs(self, username, password, msg, memcachekey):
				"""
				send baidu msgs. use baidu username, password.
				the msgs parameter is a message list, not a single string.
				"""
				cookie = ''
				if memcache.get(memcachekey):
						cookie = memcache.get(memcachekey)
				else:
						try:
								form_fields = {
										"UserLoginForm[username]": username,
										"UserLoginForm[password]":password,
										"UserLoginForm[rememberMe]":1
										}
								form_data = urllib.urlencode(form_fields)
								url = 'http://t.163.com/statuses/update.do'
								headers = {'Referer':'http://t.baidu.com/',
												'Content-Type': 'application/x-www-form-urlencoded',
												'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13'
											}
								req = urllib2.Request(url, form_data, headers)
								result = urllib2.urlopen(req)
						except Exception:
								return False
						if result.status_code == 302:
							pass
						else:
							return False
						cookie = Cookie.SimpleCookie(result.headers.get('set-cookie', ''))
						callback_url = result.headers.get('location', '')
						cookie = self.make_cookie_header(cookie)
						#result,cookie = self.do_redirect(callback_url, cookie)
						memcache.set(memcachekey, cookie, 36000)
				self.Add_baidu_firend(cookie)
				msg = unescape(msg)
				form_fields = {
						"m_content":msg,
						"pic_id":0,
						"pic_filename":'',
						"pic_id_water":0,
						"pic_filename_water":'',
				}
				form_data = urllib.urlencode(form_fields)
				url = 'http://t.baidu.com/message/post'
				headers = {'Referer':'http://t.baidu.com/', 'Cookie' : cookie}
				try:
					req = urllib2.Request(url, form_data, headers)
					result = urllib2.urlopen(req)
				except Exception, data:
							logging.info(data)
							return False
				if result.status_code == 200:
							return True
				else:
							return False
		
		def Get_qzone2(self, model, pushitem, **kwargs):
				"""
				this method is used to get login to website,and put the content to the qzone
				"""
				try:


					contenthtml = u'%s 详细内容请查看：<a herf=%s>%s</a>' % (
								htmllib.decoding(htmllib.Filter_html(model.content)),
								unicode(model.fullurl), unicode(model.fullurl))
					contenthtml = htmllib.encoding(contenthtml, 'gb18030')
					title = htmllib.encoding(htmllib.decoding(model.title), 'gb18030')
					content = htmllib.Filter_html(contenthtml)
					#content=html
					result = self.send_qzone2(pushitem.username, pushitem.password, content, title, contenthtml)
					if result:
						return self.Get_True(model, pushitem)
					else:
						return self.Get_False(model, pushitem)
				except Exception, data:
						return self.Get_False(model, pushitem, data)

		def Get_qzone2_val(self, username, password):
				verifyURL = 'http://ptlogin2.qq.com/check?uin=%s&appid=15000101' % username
				loginURL = 'http://ptlogin2.qq.com/login?'
				redirectURL = ''
				cookie = ''
				qqn = username
				md5Pass = ''
				verifyCode = ''
				result = urllib2.urlopen(url=verifyURL, method=urlfetch.GET,
						follow_redirects=False, headers={
						'Content-Type': 'application/x-www-form-urlencoded',
						'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13',
						},)
				cookie1 = Cookie.SimpleCookie(result.headers.get('set-cookie', ''))
				verifyCode = result.content[18:-3]
				loginURL += "u=%s&p=" % username
				loginURL += self.EncodePasswordWithVerifyCode(password, verifyCode)
				loginURL += "&verifycode=" + verifyCode + "&aid=15000101&u1=http%3A%2F%2Fimgcache.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&ptredirect=1&h=1&from_ui=1&fp=loginerroralert"
				result = urllib2.urlopen(url=loginURL,
						headers={'Referer':'http://t.qq.com',
						'Cookie' : self.make_cookie_header(cookie1),
						'Content-Type': 'application/x-www-form-urlencoded',
						'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13',
						},
						method=urlfetch.GET,
						follow_redirects=False,
				)

				setCookies = result.headers.get('set-cookie', '').split(';')
				cookie2 = ''
				cookie2 += setCookies[29]
				cookie2 += setCookies[7]
				cookie2 += setCookies[4]
				cookie2 += ';' + setCookies[0]
				cookie2 = cookie2.replace(',', ';')
				cookie2 = cookie2[1:]
				callback_url = result.headers.get('location', 'http://imgcache.qq.com/qzone/v5/loginsucc.html?para=izone')
				result, cookie = self.do_redirect(callback_url, cookie2)


				return result, cookie
		def Tmp_skey_get(self, cookie):
				tmp = cookie.split(';')
				for i in tmp:
						if i[1:5] == 'skey':
								return i[6:]
				return None


		def send_qzone2(self, username, password, content, title, html):
			"""
			send qzone blog. use  username, password,content,title,html.
			the content parameter like html,but no html tag.
			"""
			memcachekey = 'send_qzone2'
			cookie = ''
			if memcache.get(memcachekey):
				cookie = memcache.get(memcachekey)
				logging.info('get cookie from memcache')
			else:
				result, oldcookie = self.Get_qzone2_val(username, password)
				cookie = '%s;%s' % (result.headers.get('set-cookie', ''), oldcookie)
				memcache.set(memcachekey, cookie, 36000)
				logging.info('set cookie')
				
			tmphash = self.Tmp_skey_get(cookie)
			tmphash = self.myhash(tmphash)
			category = '个人日记'
			form_fields = {
				"uin":'939567050',
				"category":htmllib.encoding(category, 'gb18030'),
				"title":title,
				"content":content,
				"html":html,
				"cb_autograph":'1',
				"topflag":'0',
				"needfeed":'0',
				"lp_type":'0',
				"g_tk":tmphash,
				"scorr_20100723_":'http://qzs.qq.com/qzone/newblog/v5/editor.html|http://qzs.qq.com/qzone/newblog/v5/editor.html<http://user.qzone.qq.com/939567050/main',
			}
			form_data = urllib.urlencode(form_fields)
			try:
				result = urllib2.urlopen(url="http://b.qzone.qq.com/cgi-bin/blognew/blog_add",
								payload=form_data,
								method=urlfetch.POST,
								headers={'Referer':'http://imgcache.qq.com/qzone/v5/toolpages/fp_gbk.html',
								'Cookie' : cookie,
								'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13',

								}, follow_redirects=False)
			except Exception, data:
						logging.info(data)
						return False
			if result.status_code == 200:
						return True
			else:
						return False

		def make_cookie_header2(self, cookie):
				ret = ""
				for val in cookie.values():
						ret += "%s=%s; " % (val.split('=')[0], val.split('=')[1])
				return ret


		def Make_cookie_dict(self, cookie):
				tmpval = dict()
				for val in cookie:
						tmpval.update({val.split('=')[0]:val.split('=')[1]})
				return tmpval

		def md5hash(self, str):
				return hashlib.md5(str).digest()
		def hex_md5hash(self, str):
				return hashlib.md5(str).hexdigest().upper()
		def md5hash_3(self, str):
				return self.hex_md5hash(self.md5hash(self.md5hash(str)))
		def EncodePasswordWithVerifyCode(self, pwd, verifyCode):
				return self.hex_md5hash(self.md5hash_3(pwd) + verifyCode.upper())

		def Get_qq_msg_val(self, username, password):
				verifyURL = 'http://ptlogin2.qq.com/check?uin=%s&appid=46000101&r=%s' % (username, random.random())
				loginURL = 'http://ptlogin2.qq.com/login?'
				redirectURL = ''
				cookie = ''
				qqn = username
				md5Pass = ''
				verifyCode = ''
				result = urllib2.urlopen(url=verifyURL, method=urlfetch.GET,
						follow_redirects=False, headers={
						'Content-Type': 'application/x-www-form-urlencoded',
						'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13',
						},)
				cookie1 = Cookie.SimpleCookie(result.headers.get('set-cookie', ''))
				verifyCode = result.content[18:-3]
				if len(verifyCode) > 4:
						return False, None
				loginURL += "u=%s&p=" % username
				loginURL += self.EncodePasswordWithVerifyCode(password, verifyCode)
				loginURL += "&verifycode=" + verifyCode + "&aid=46000101&u1=http%3A%2F%2Ft.qq.com&ptredirect=1&h=1&from_ui=1&fp=loginerroralert"
				result = urllib2.urlopen(url=loginURL,
						headers={'Referer':'http://t.qq.com',
						'Cookie' : self.make_cookie_header(cookie1),
						'Content-Type': 'application/x-www-form-urlencoded',
						'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13',
						},
						method=urlfetch.GET,
						follow_redirects=False,
				)
				setCookies = result.headers.get('set-cookie', '').split(';')
				cookie2 = ''
				cookie2 += setCookies[29]
				cookie2 += setCookies[7]
				cookie2 += setCookies[4]
				cookie2 += ';' + setCookies[0]
				cookie2 = cookie2.replace(',', ';')
				cookie2 = cookie2[1:]
				callback_url = result.headers.get('location', 'http://t.qq.com')
				result, cookies = self.do_redirect(callback_url, cookie2)

				return result, cookies


		def do_redirect(self, url, cookie):
			url = url
			headers = {'Cookie':cookie,
					'Content-Type': 'application/x-www-form-urlencoded',
					'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13', }
			req = urllib2.Request(url, form_data, headers)
			result = urllib2.urlopen(req)
				
			return result, cookie

		def send_qq_msgs(self, username, password, msg, memcachekey):
			"""
			send sina msgs. use qq username, password.
			the msgs parameter is a message list, not a single string.
			"""
			cookie = ''
			if memcache.get(memcachekey):
				cookie = memcache.get(memcachekey)
			else:
				result, oldcookie = self.Get_qq_msg_val(username, password)
				if result == False:
					return False
				cookie = '%s;%s' % (result.headers.get('set-cookie', ''), oldcookie)
				memcache.set(memcachekey, cookie, 36000)
			msg = unescape(msg)
			form_fields = {
			  "content": msg,
			  "pic":'',
			  "countType":'',
			  "viewModel":1
			}
			form_data = urllib.urlencode(form_fields)
			url = 'http://t.qq.com/publish.php?rnd=0.5100760071072727'
			headers = {'Referer':'http://t.qq.com',
								'Cookie' : cookie,
								'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13',

								}
			try:
				req = urllib2.Request(url, form_data, headers)
				result = urllib2.urlopen(req)
			except:
						return False
			if result.status_code == 200:
						return True
			else:
						return False

		def myhash(self, tmpvalue):
				tmphash = 5381
				if not tmpvalue is None:
						tmpvalue = tmpvalue
						for i in range(0, len(tmpvalue)):
								tmphash += (tmphash << 5) + ord(tmpvalue[i])
						return (tmphash & 0x7FFFFFFF)
				else:
						return False




def unescape(text):
   """Removes HTML or XML character references
      and entities from a text string.
   from Fredrik Lundh
   http://effbot.org/zone/re-sub.htm#unescape-html
   """
   def fixup(m):
       text = m.group(0)
       if text[:2] == "&#":
           # character reference
           try:
               if text[:3] == "&#x":
                   return unichr(int(text[3:-1], 16))
               else:
                   return unichr(int(text[2:-1]))
           except ValueError:
               pass
       else:
           # named entity
           try:
               text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
           except KeyError:
               pass
       return text # leave as is
   return re.sub("&#?\w+;", fixup, text)
