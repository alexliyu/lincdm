"""XML-RPC methods for Zinnia"""


ZINNIA_XMLRPC_PINGBACK = [
    ('app.zinnia.xmlrpc.pingback.pingback_ping',
     'pingback.ping'),
    ('app.zinnia.xmlrpc.pingback.pingback_extensions_get_pingbacks',
     'pingback.extensions.getPingbacks')]

ZINNIA_XMLRPC_METAWEBLOG = [
    ('app.zinnia.xmlrpc.metaweblog.get_users_blogs',
     'blogger.getUsersBlogs'),
    ('app.zinnia.xmlrpc.metaweblog.get_user_info',
     'blogger.getUserInfo'),
    ('app.zinnia.xmlrpc.metaweblog.delete_post',
     'blogger.deletePost'),
    ('app.zinnia.xmlrpc.metaweblog.get_authors',
     'wp.getAuthors'),
    ('app.zinnia.xmlrpc.metaweblog.get_categories',
     'metaWeblog.getCategories'),
    ('app.zinnia.xmlrpc.metaweblog.new_category',
     'wp.newCategory'),
    ('app.zinnia.xmlrpc.metaweblog.get_recent_posts',
     'metaWeblog.getRecentPosts'),
    ('app.zinnia.xmlrpc.metaweblog.get_post',
     'metaWeblog.getPost'),
    ('app.zinnia.xmlrpc.metaweblog.new_post',
     'metaWeblog.newPost'),
    ('app.zinnia.xmlrpc.metaweblog.edit_post',
     'metaWeblog.editPost'),
    ('app.zinnia.xmlrpc.metaweblog.new_media_object',
     'metaWeblog.newMediaObject')]

ZINNIA_XMLRPC_METHODS = ZINNIA_XMLRPC_PINGBACK + ZINNIA_XMLRPC_METAWEBLOG
