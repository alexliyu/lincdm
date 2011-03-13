import sys, os

from gevent import wsgi 
from gevent import socket 
from gevent import monkey

sys.stdout = sys.stderr

# Just in case 
monkey.patch_all()

import pwd

# Get this so we can chown/chgrp the socket and let nginx read it 
pe = pwd.getpwnam('www-data')

SOCK = '/home/alex/lincdm/lincdm/server.sock'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) 
try: 
    os.remove(SOCK) 
except OSError: 
    pass

sock.bind(SOCK) 
os.chown(SOCK, pe.pw_uid, pe.pw_gid) 
os.chmod(SOCK, 0770) 
sock.listen(256)

import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler() 
print application 
# Set up for Django 
sys.path.insert(0, '/home/alex/lincdm/') 
sys.path.insert(0, '/home/alex/lincdm/lincdm/') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'lincdm.settings' 

#wsgi.WSGIServer(sock, application, spawn=None).serve_forever() 
wsgi.WSGIServer(sock, application).serve_forever()
