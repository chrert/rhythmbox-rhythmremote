'''
Created on 06.10.2012

@author: chri
'''

from gi.repository import GObject

class IWebServer():
    _host = None
    _port = None
    
    _is_running = False

    def __init__(self, host, port, settings):
        self._host = host
        self._port = port
        self._is_running = False
        
    def run(self):
        self._start_server()
        
    def start(self):
        raise NotImplementedError("IWebServer is abstract")
        
    def stop(self):
        raise NotImplementedError("IWebServer is abstract")
        
    def is_running(self):
        return self._is_running
        
    def _start_server(self):
        raise NotImplementedError("IWebServer is abstract")

from wsgiref.simple_server import make_server
import bottle

class WSGIRefWebServer(IWebServer):
    def __init__(self, host, port, settings):
        IWebServer.__init__(self, host, port, settings)

    def _start_server(self):
        wsgi_handler = bottle.default_app()
        self.__server = make_server(self._host, self._port, wsgi_handler)
        self._is_running = True
        
        def request_loop(source, cb):
            self.__server.handle_request()
            return True
        
        self.watch_id = GObject.io_add_watch(self.__server.socket, GObject.IO_IN, request_loop)
        
    def start(self):
        self.run()
        
    def stop(self):
        GObject.source_remove(self.watch_id)
        self._is_running = False

"""
import threading
from tornado import httpserver, ioloop, wsgi

class TornadoWebServer(IWebServer, threading.Thread):
    def __init__(self, host, port, settings):
        IWebServer.__init__(self, host, port, settings)
        threading.Thread.__init__(self)
        
    def _start_server(self):
        django_handler = django.core.handlers.wsgi.WSGIHandler()
        container = wsgi.WSGIContainer(django_handler)
        self.__server = httpserver.HTTPServer(container)
        self.__server.listen(self._port)
        self._is_running = True
        ioloop.IOLoop.instance().start()
        
    def start(self):
        threading.Thread.start(self)
        
    def stop(self):
        pass
"""

from Views import add_template_path
add_template_path("web/")