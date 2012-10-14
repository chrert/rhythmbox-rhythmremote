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


def add_template_path(path):
    bottle.TEMPLATE_PATH.append(os.path.abspath(path))

@bottle.route("/script/<filepath:path>")
def static_script(filepath):
    filepath = urllib.unquote_plus(filepath);
    return bottle.static_file(filepath, root=os.path.abspath("web/script") + "/")

@bottle.route("/")
@bottle.view("artists")
def index():
    return dict(artists=order_set(DBAccess().get_all_artists()))

@bottle.route("/albums/<artist>")
@bottle.view("albums")
def albums(artist):
    artist = urllib.unquote_plus(artist)
    return dict(albums=order_set(DBAccess().get_albums_of_artist(artist)),
                artist=artist,
                backlink=("/", "Artists"))

@bottle.route("/tracks/<artist>/<album>")
@bottle.view("tracks")
def tracks(artist, album):
    artist = urllib.unquote_plus(artist)
    album = urllib.unquote_plus(album)
    return dict(tracks=order_set(DBAccess().get_tracks_of_album(artist, album)),
                backlink=("/albums/" + artist, artist))

@bottle.route("/play/<entry_id:int>")
def play_entry(entry_id):
    player = PlayerControl()
    player.play_entry(entry_id)
    return "1"

@bottle.route("/add_to_queue/<entry_id:int>")
def add_to_queue(entry_id):
    PlayerControl().add_entry_to_queue(entry_id)
    return "1"

@bottle.route("/play")
def play():
    PlayerControl().play()

@bottle.route("/prev")
def play_previous():
    PlayerControl().previous()
    
@bottle.route("/next")
def play_next():
    PlayerControl().next()
    
@bottle.route("/pause")
def pause():
    PlayerControl().pause()
    
@bottle.route("/stop")
def stop():
    PlayerControl().stop()

@bottle.route("/seek/<position:int>")
def seek(position):
    PlayerControl().seek(position)

@bottle.route("/volume")
def get_volume():
    return str(PlayerControl().get_volume())

@bottle.route("/volume/<volume:float>")
def set_volume(volume):
    player = PlayerControl()
    player.set_volume(volume)
    return str(player.get_volume())

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
            "position"     : player.get_playing_time()}

def order_set(_set):
    return sorted(list(_set))
