"""XML-RPC methods for blog"""


blog_XMLRPC_PINGBACK = [
    ('app.blog.xmlrpc.pingback.pingback_ping',
     'pingback.ping'),
    ('app.blog.xmlrpc.pingback.pingback_extensions_get_pingbacks',
     'pingback.extensions.getPingbacks')]

blog_XMLRPC_METAWEBLOG = [
    ('app.blog.xmlrpc.metaweblog.get_users_blogs',
     'blogger.getUsersBlogs'),
    ('app.blog.xmlrpc.metaweblog.get_user_info',
     'blogger.getUserInfo'),
    ('app.blog.xmlrpc.metaweblog.delete_post',
     'blogger.deletePost'),
    ('app.blog.xmlrpc.metaweblog.get_authors',
     'wp.getAuthors'),
    ('app.blog.xmlrpc.metaweblog.get_categories',
     'metaWeblog.getCategories'),
    ('app.blog.xmlrpc.metaweblog.new_category',
     'wp.newCategory'),
    ('app.blog.xmlrpc.metaweblog.get_recent_posts',
     'metaWeblog.getRecentPosts'),
    ('app.blog.xmlrpc.metaweblog.get_post',
     'metaWeblog.getPost'),
    ('app.blog.xmlrpc.metaweblog.new_post',
     'metaWeblog.newPost'),
    ('app.blog.xmlrpc.metaweblog.edit_post',
     'metaWeblog.editPost'),
    ('app.blog.xmlrpc.metaweblog.new_media_object',
     'metaWeblog.newMediaObject')]

blog_XMLRPC_METHODS = blog_XMLRPC_PINGBACK + blog_XMLRPC_METAWEBLOG
