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

import bottle, os, urllib
from WebPlayer import DBAccess, PlayerControl

class Views:
    
    rbplugin = None;
    
    @staticmethod 
    def add_template_path(path):
        try:
            web_path = Views.rbplugin.find_file(path)
            
            if web_path is None:
                web_path = os.path.abspath(path)
                print "Cant't find web folder! Using: " + web_path
                
            bottle.TEMPLATE_PATH.append(web_path)
        except NameError:
            print "You need to assign Views.rbplugin first!"
            raise
        
    @staticmethod
    @bottle.route("/script/<filepath:path>")
    def static_script(filepath):
        filepath = urllib.unquote_plus(filepath);
        script_path = ""
        try:
            script_path = Views.rbplugin.find_file("web/script/")
            
            if script_path is None:
                script_path = os.path.abspath("web/script") + "/"
                print "Cant't find script folder! Using: " + script_path
                
            return bottle.static_file(filepath, root=script_path)
        except NameError:
            print "You need to assign Views.rbplugin first!"
            raise
    
    @staticmethod
    @bottle.route("/")
    @bottle.view("artists")
    def index():
        return dict(artists=order_set(DBAccess().get_all_artists()))
    
    @staticmethod
    @bottle.route("/albums/<artist:path>")
    @bottle.view("albums")
    def albums(artist):
        artist = urllib.unquote_plus(artist)
        return dict(albums=order_set(DBAccess().get_albums_of_artist(artist)),
                    artist=artist,
                    backlink=("/", "Artists"))
    
    @staticmethod
    @bottle.route("/tracks/<artist:path>/<album:path>")
    @bottle.view("tracks")
    def tracks(artist, album):
        artist = urllib.unquote_plus(artist)
        album = urllib.unquote_plus(album)
        return dict(tracks=order_track_set(DBAccess().get_tracks_of_album(artist, album)),
                    backlink=("/albums/" + artist, artist))
    
    @staticmethod
    @bottle.route("/playlist/<playlist:path>")
    @bottle.view("playlist")
    def playlist(playlist):
        playlist = urllib.unquote_plus(playlist)
        return dict(tracks=PlayerControl().get_playlist_entries(playlist),
                    playlist=playlist,
                    backlink=("/", "Home"))
        
    @staticmethod
    @bottle.route("/play/<entry_id:int>")
    def play_entry(entry_id):
        player = PlayerControl()
        player.play_entry(entry_id)
        return "1"
    
    @staticmethod
    @bottle.route("/add_to_queue/<entry_id:int>")
    def add_to_queue(entry_id):
        PlayerControl().add_entry_to_queue(entry_id)
        return "1"
    
    @staticmethod
    @bottle.route("/play")
    def play(self):
        PlayerControl().play()
    
    @staticmethod 
    @bottle.route("/play_queue/<entry_id:int>")
    def play_queue(entry_id):
        PlayerControl().play_entry_from_queue(entry_id)
    
    @staticmethod
    @bottle.route("/play/<playlist>/<entry_id:int>")
    def play_playlist_entry(playlist, entry_id):
        PlayerControl().play_entry_from_playlist(entry_id, playlist)
    
    @staticmethod
    @bottle.route("/prev")
    def play_previous():
        PlayerControl().previous()
    
    @staticmethod
    @bottle.route("/next")
    def play_next():
        PlayerControl().next()
    
    @staticmethod
    @bottle.route("/pause")
    def pause():
        PlayerControl().pause()
    
    @staticmethod
    @bottle.route("/stop")
    def stop():
        PlayerControl().stop()
        
    @staticmethod
    @bottle.route("/seek/<position:int>")
    def seek(position):
        PlayerControl().seek(position)
    
    @staticmethod
    @bottle.route("/volume")
    def get_volume():
        return str(PlayerControl().get_volume())
    
    @staticmethod
    @bottle.route("/volume/<volume:float>")
    def set_volume(volume):
        player = PlayerControl()
        player.set_volume(volume)
        return str(player.get_volume())
    
    @staticmethod
    @bottle.route("/playerinfo")
    def get_player_info():
        player = PlayerControl()
        return {"volume"       : player.get_volume(),
                "playing"      : player.is_playing(),
                "play_or_pause": player.get_playing_entry_id() >= 0,
                "has_next"     : player.has_next(),
                "has_prev"     : player.has_prev(),
                "title"        : player.get_playing_entry_str(),
                "duration"     : player.get_playing_duration(),
                "position"     : player.get_playing_time(),
                "queue_entries": player.get_queue_entries(),
                "playlists"    : player.get_playlist_names()}
    
def order_set(_set):
    return sorted(list(_set))
    
def order_track_set(_set):
    return sorted(list(_set), cmp=lambda x,y: cmp(x[1], y[1]))
