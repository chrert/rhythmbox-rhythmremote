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

#import rb #module not found    
from gi.repository import GObject, Peas
import os

import WebPlayer, Views
from WebServer import WSGIRefWebServer as WebServer

class RhythmRemotePlugin(GObject.Object, Peas.Activatable):
    object = GObject.Property(type=GObject.Object)
    
    def __init__(self):
        super(RhythmRemotePlugin, self).__init__()
        
    def do_activate(self):
        WebPlayer.DBAccess.rbshell = self.object;
        WebPlayer.PlayerControl.rbshell = self.object
        Views.Views.rbplugin = self
        Views.Views.add_template_path("web/")
        
        print "starting server..."    
        self.__server = WebServer("0.0.0.0", 8001, "webplayer.settings")
        self.__server.start()
        
    def do_deactivate(self):
        print "stopping server..."
        
    def find_file(self, filename):
        info = self.plugin_info
        data_dir = info.get_data_dir()
        data_dir = data_dir.replace("/src", "/rhythmremote/")
        path = os.path.join(data_dir, filename)
        
        if os.path.exists(path):
            return path
        
        return None
