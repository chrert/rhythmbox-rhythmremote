# ------------------------------------------------------------------------------
# - Copyright (c) 2012 Christian Ertler.
# - All rights reserved. This program and the accompanying materials
# - are made available under the terms of the GNU Public License v3.0
# - which accompanies this distribution, and is available at
# - http://www.gnu.org/licenses/gpl.html
# - 
# - Contributors:
# -     Christian Ertler - initial API and implementation
# ------------------------------------------------------------------------------

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
