#!/usr/bin/env python
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
from app.blog.models import EntryAbstractClass as Entry
from app.pushblog.models import PushList, PushMethod
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

class Command(BaseCommand):
	def handle(self, *args, **options):
		if not len(args):
			print "You must provide the feed url as parameter"
			exit(0)
		feed_url = args[0]
		# process feed in create-mode
		Pusharticle.Push(self)
		
class Pusharticle:


		def Push(self, page=None, *arg1, **arg2):
				listits = PushList.objects.values_list()
				logging.info('start to Push Article')
				for pushitem in listits:
						push_retrieval_deadline = datetime.now() - timedelta(minutes=pushitem.pushtime)
						if pushitem.last_retrieved > push_retrieval_deadline:
							logging.info('Skipping entry %s.', pushitem.name)
							continue
						try:
								if pushitem.latest:
										entry = Entry.objects.all().filter('categories = ', pushitem.category).filter('date > ', pushitem.latest).order('date').fetch(1)[0]
								else:
										entry = Entry.objects.all().filter('categories = ', pushitem.category).order('date').fetch(1)[0]
						except:
								entry = None
						if entry:

								logging.info('Getting entry %s.', entry.title)
								kwargs = dict((['model', entry],
										['pushitem', pushitem]
										))
								result = PushMethod().Get_Method(pushitem.pushurl, **kwargs)
								if result:
										logging.info('Pushed Successful')
								else:
										logging.info('Pushed Fail')

						else:
								logging.info('no entry')
