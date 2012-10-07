from gi.repository import GObject, RB, Peas

import WebPlayer
from WebServer import WSGIRefWebServer as WebServer

class WebPlayerPlugin(GObject.Object, Peas.Activatable):
    object = GObject.Property(type=GObject.Object)
    
    def __init__(self):
        super(WebPlayerPlugin, self).__init__()
        
    def do_activate(self):
        WebPlayer.initialize(self.object)
        
        print "starting server..."    
        self.__server = WebServer("localhost", 8001, "webplayer.settings")
        self.__server.start()
        
    def do_deactivate(self):
        print "stopping server..."