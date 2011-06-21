"""XML-RPC methods for blog"""


blog_XMLRPC_PINGBACK = [
    ('blog.xmlrpc.pingback.pingback_ping',
     'pingback.ping'),
    ('blog.xmlrpc.pingback.pingback_extensions_get_pingbacks',
     'pingback.extensions.getPingbacks')]

blog_XMLRPC_METAWEBLOG = [
    ('blog.xmlrpc.metaweblog.get_users_blogs',
     'blogger.getUsersBlogs'),
    ('blog.xmlrpc.metaweblog.get_user_info',
     'blogger.getUserInfo'),
    ('blog.xmlrpc.metaweblog.delete_post',
     'blogger.deletePost'),
    ('blog.xmlrpc.metaweblog.get_authors',
     'wp.getAuthors'),
    ('blog.xmlrpc.metaweblog.get_categories',
     'metaWeblog.getCategories'),
    ('blog.xmlrpc.metaweblog.new_category',
     'wp.newCategory'),
    ('blog.xmlrpc.metaweblog.get_recent_posts',
     'metaWeblog.getRecentPosts'),
    ('blog.xmlrpc.metaweblog.get_post',
     'metaWeblog.getPost'),
    ('blog.xmlrpc.metaweblog.new_post',
     'metaWeblog.newPost'),
    ('blog.xmlrpc.metaweblog.edit_post',
     'metaWeblog.editPost'),
    ('blog.xmlrpc.metaweblog.new_media_object',
     'metaWeblog.newMediaObject')]

blog_XMLRPC_METHODS = blog_XMLRPC_PINGBACK + blog_XMLRPC_METAWEBLOG
