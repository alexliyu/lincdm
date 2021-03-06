"""XML-RPC methods of entry metaWeentry API"""
import os
from datetime import datetime
from xmlrpclib import Fault
from xmlrpclib import DateTime

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.translation import gettext as _
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.template.defaultfilters import slugify

from lincdm.entry.models import Entry
from lincdm.entry.models import Category
from lincdm.settings import PROTOCOL
from lincdm.settings import UPLOAD_TO
from lincdm.managers import DRAFT, PUBLISHED
from django_xmlrpc.decorators import xmlrpc_func

# http://docs.nucleuscms.org/entry/12#errorcodes
LOGIN_ERROR = 801
PERMISSION_DENIED = 803


def authenticate(username, password, permission=None):
    """Authenticate staff_user with permission"""
    try:
        user = User.objects.get(username__exact=username)
    except User.DoesNotExist:
        raise Fault(LOGIN_ERROR, _('Username is incorrect.'))
    if not user.check_password(password):
        raise Fault(LOGIN_ERROR, _('Password is invalid.'))
    if not user.is_staff or not user.is_active:
        raise Fault(PERMISSION_DENIED, _('User account unavailable.'))
    if permission:
        if not user.has_perm(permission):
            raise Fault(PERMISSION_DENIED, _('User cannot %s.') % permission)
    return user


def entry_structure(site):
    """A entry structure"""
    return {'url': '%s://%s%s' % (
        PROTOCOL, site.domain, reverse('index')),
            'entryid': settings.SITE_ID,
            'entryName': site.name}


def user_structure(user, site):
    """An user structure"""
    return {'userid': user.pk,
            'email': user.email,
            'nickname': user.username,
            'lastname': user.last_name,
            'firstname': user.first_name,
            'url': '%s://%s%s' % (
                PROTOCOL, site.domain,
                reverse('entry_author_detail', args=[user.username]))}


def author_structure(user):
    """An author structure"""
    return {'user_id': user.pk,
            'user_login': user.username,
            'display_name': user.username,
            'user_email': user.email}


def category_structure(category, site):
    """A category structure"""
    return {'description': category.title,
            'htmlUrl': '%s://%s%s' % (
                PROTOCOL, site.domain,
                category.get_absolute_url()),
            'rssUrl': '%s://%s%s' % (
                PROTOCOL, site.domain,
                reverse('entry_category_feed', args=[category.tree_path])),
            # Useful Wordpress Extensions
            'categoryId': category.pk,
            'parentId': category.parent and category.parent.pk or 0,
            'categoryDescription': category.description,
            'categoryName': category.title}


def post_structure(entry, site):
    """A post structure with extensions"""
    author = entry.authors.all()[0]
    return {'title': entry.title,
            'description': unicode(entry.html_content),
            'link': '%s://%s%s' % (PROTOCOL, site.domain,
                                   entry.get_absolute_url()),
            # Basic Extensions
            'permaLink': '%s://%s%s' % (PROTOCOL, site.domain,
                                        entry.get_absolute_url()),
            'categories': [cat.title for cat in entry.categories.all()],
            'dateCreated': DateTime(entry.creation_date.isoformat()),
            'postid': entry.pk,
            'userid': author.username,
            # Useful Movable Type Extensions
            'mt_excerpt': entry.excerpt,
            'mt_allow_comments': int(entry.comment_enabled),
            'mt_allow_pings': int(entry.pingback_enabled),
            'mt_keywords': entry.tags,
            # Useful Wordpress Extensions
            'wp_author': author.username,
            'wp_author_id': author.pk,
            'wp_author_display_name': author.username,
            'wp_password': entry.password,
            'wp_slug': entry.slug,
            'sticky': entry.featured}


@xmlrpc_func(returns='struct[]', args=['string', 'string', 'string'])
def get_users_entrys(apikey, username, password):
    """entryger.getUsersBlogs(api_key, username, password)
    => entry structure[]"""
    authenticate(username, password)
    site = Site.objects.get_current()
    return [entry_structure(site)]


@xmlrpc_func(returns='struct', args=['string', 'string', 'string'])
def get_user_info(apikey, username, password):
    """entryger.getUserInfo(api_key, username, password)
    => user structure"""
    user = authenticate(username, password)
    site = Site.objects.get_current()
    return user_structure(user, site)


@xmlrpc_func(returns='struct[]', args=['string', 'string', 'string'])
def get_authors(apikey, username, password):
    """wp.getAuthors(api_key, username, password)
    => author structure[]"""
    authenticate(username, password)
    return [author_structure(author)
            for author in User.objects.filter(is_staff=True)]


@xmlrpc_func(returns='boolean', args=['string', 'string',
                                      'string', 'string', 'string'])
def delete_post(apikey, post_id, username, password, publish):
    """entryger.deletePost(api_key, post_id, username, password, 'publish')
    => boolean"""
    user = authenticate(username, password, 'entry.delete_entry')
    entry = Entry.objects.get(id=post_id, authors=user)
    entry.delete()
    return True


@xmlrpc_func(returns='struct', args=['string', 'string', 'string'])
def get_post(post_id, username, password):
    """metaWeentry.getPost(post_id, username, password)
    => post structure"""
    user = authenticate(username, password)
    site = Site.objects.get_current()
    return post_structure(Entry.objects.get(id=post_id, authors=user), site)


@xmlrpc_func(returns='struct[]',
             args=['string', 'string', 'string', 'integer'])
def get_recent_posts(entry_id, username, password, number):
    """metaWeentry.getRecentPosts(entry_id, username, password, number)
    => post structure[]"""
    user = authenticate(username, password)
    site = Site.objects.get_current()
    return [post_structure(entry, site) \
            for entry in Entry.objects.filter(authors=user)[:number]]


@xmlrpc_func(returns='struct[]', args=['string', 'string', 'string'])
def get_categories(entry_id, username, password):
    """metaWeentry.getCategories(entry_id, username, password)
    => category structure[]"""
    authenticate(username, password)
    site = Site.objects.get_current()
    return [category_structure(category, site) \
            for category in Category.objects.all()]


@xmlrpc_func(returns='string', args=['string', 'string', 'string', 'struct'])
def new_category(entry_id, username, password, category_struct):
    """wp.newCategory(entry_id, username, password, category)
    => category_id"""
    authenticate(username, password, 'entry.add_category')
    category_dict = {'title': category_struct['name'],
                     'description': category_struct['description'],
                     'slug': category_struct['slug']}
    if int(category_struct['parent_id']):
        category_dict['parent'] = Category.objects.get(
            pk=category_struct['parent_id'])
    category = Category.objects.create(**category_dict)

    return category.pk


@xmlrpc_func(returns='string', args=['string', 'string', 'string',
                                     'struct', 'boolean'])
def new_post(entry_id, username, password, post, publish):
    """metaWeentry.newPost(entry_id, username, password, post, publish)
    => post_id"""
    user = authenticate(username, password, 'entry.add_entry')
    if post.get('dateCreated'):
        creation_date = datetime.strptime(
            post['dateCreated'].value.replace('Z', '').replace('-', ''),
            '%Y%m%dT%H:%M:%S')
    else:
        creation_date = datetime.now()

    entry_dict = {'title': post['title'],
                  'content': post['description'],
                  'excerpt': post.get('mt_excerpt', truncate_words(
                      strip_tags(post['description']), 50)),
                  'creation_date': creation_date,
                  'last_update': creation_date,
                  'comment_enabled': post.get('mt_allow_comments', 1) == 1,
                  'pingback_enabled': post.get('mt_allow_pings', 1) == 1,
                  'featured': post.get('sticky', 0) == 1,
                  'tags': 'mt_keywords' in post and post['mt_keywords'] or '',
                  'slug': 'wp_slug' in post and post['wp_slug'] or slugify(
                      post['title']),
                  'password': post.get('wp_password', ''),
                  'status': publish and PUBLISHED or DRAFT}
    entry = Entry.objects.create(**entry_dict)

    author = user
    if 'wp_author_id' in post and user.has_perm('entry.can_change_author'):
        if int(post['wp_author_id']) != user.pk:
            author = User.objects.get(pk=post['wp_author_id'])
    entry.authors.add(author)

    entry.sites.add(Site.objects.get_current())
    if 'categories' in post:
        entry.categories.add(*[Category.objects.get_or_create(
            title=cat, slug=slugify(cat))[0]
                               for cat in post['categories']])

    return entry.pk


@xmlrpc_func(returns='boolean', args=['string', 'string', 'string',
                                      'struct', 'boolean'])
def edit_post(post_id, username, password, post, publish):
    """metaWeentry.editPost(post_id, username, password, post, publish)
    => boolean"""
    user = authenticate(username, password, 'entry.change_entry')
    entry = Entry.objects.get(id=post_id, authors=user)
    if post.get('dateCreated'):
        creation_date = datetime.strptime(
            post['dateCreated'].value.replace('Z', '').replace('-', ''),
            '%Y%m%dT%H:%M:%S')
    else:
        creation_date = entry.creation_date

    entry.title = post['title']
    entry.content = post['description']
    entry.excerpt = post.get('mt_excerpt', truncate_words(
        strip_tags(post['description']), 50))
    entry.creation_date = creation_date
    entry.last_update = datetime.now()
    entry.comment_enabled = post.get('mt_allow_comments', 1) == 1
    entry.pingback_enabled = post.get('mt_allow_pings', 1) == 1
    entry.featured = post.get('sticky', 0) == 1
    entry.tags = 'mt_keywords' in post and post['mt_keywords'] or ''
    entry.slug = 'wp_slug' in post and post['wp_slug'] or slugify(
        post['title'])
    entry.status = publish and PUBLISHED or DRAFT
    entry.password = post.get('wp_password', '')
    entry.save()

    if 'wp_author_id' in post and user.has_perm('entry.can_change_author'):
        if int(post['wp_author_id']) != user.pk:
            author = User.objects.get(pk=post['wp_author_id'])
            entry.authors.clear()
            entry.authors.add(author)

    if 'categories' in post:
        entry.categories.clear()
        entry.categories.add(*[Category.objects.get_or_create(
            title=cat, slug=slugify(cat))[0]
                               for cat in post['categories']])
    return True


@xmlrpc_func(returns='struct', args=['string', 'string', 'string', 'struct'])
def new_media_object(entry_id, username, password, media):
    """metaWeentry.newMediaObject(entry_id, username, password, media)
    => media structure"""
    authenticate(username, password)
    path = default_storage.save(os.path.join(UPLOAD_TO, media['name']),
                                ContentFile(media['bits'].data))
    return {'url': default_storage.url(path)}
