from gevent.pywsgi import WSGIServer
from app import app
    
http_server = WSGIServer(('188.225.24.93', 5000), app)
http_server.serve_forever()