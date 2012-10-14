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
        self.__server = WebServer("0.0.0.0", 8001, "webplayer.settings")
        self.__server.start()
        
    def do_deactivate(self):
        print "stopping server..."
