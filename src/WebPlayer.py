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

from gi.repository import RB, GLib
        
class DBAccess(object):
    
    rbshell = None
    
    def __init__(self):
        try:
            self.library = DBAccess.rbshell.props.library_source
            self.db = DBAccess.rbshell.props.db
        except NameError:
            print "You need to assign DBAccess.rbshell first!"
            raise
        
    def get_all_artists(self):
        return self.__get_all_of_type(entry_type=RB.RhythmDBPropType.ARTIST)
        
    def get_all_genres(self):
        return self.__get_all_of_type(entry_type=RB.RhythmDBPropType.GENRE)
        
    def get_albums_of_artist(self, artist):
        query_model = self.__do_single_query(RB.RhythmDBPropType.ARTIST, artist)
        
        albums = set()
        for row in query_model:
            albums.add(row[0].get_string(RB.RhythmDBPropType.ALBUM))
            
        return albums
            
    def get_tracks_of_album(self, artist, album):
        query_model = self.__do_query([
            (RB.RhythmDBPropType.ARTIST, artist, RB.RhythmDBQueryType.EQUALS),
            (RB.RhythmDBPropType.ALBUM, album, RB.RhythmDBQueryType.EQUALS)
        ])
        
        return [
            (row[0].get_ulong(RB.RhythmDBPropType.ENTRY_ID), row[0].get_string(RB.RhythmDBPropType.TITLE)) 
        for row in query_model]
        
    def get_entry(self, entry_id):
        return self.db.entry_lookup_by_id(entry_id)
    
    def __do_single_query(self, prop, value, query_type=RB.RhythmDBQueryType.EQUALS):
        query_model = RB.RhythmDBQueryModel.new_empty(self.db)
        query = GLib.PtrArray()
        
        self.db.query_append_params(query, query_type, prop, value)
        self.db.do_full_query_parsed(query_model, query)
        
        return query_model
        
    def __do_query(self, params):
        query_model = RB.RhythmDBQueryModel.new_empty(self.db)
        query = GLib.PtrArray()
        
        for param in params:
            self.db.query_append_params(query, param[2], param[0], param[1])
        self.db.do_full_query_parsed(query_model, query)
        
        return query_model
        
    def __get_all_of_type(self, entry_type):
        entries = set()
        for row in self.library.props.base_query_model:
            entry = row[0]
            entries.add(entry.get_string(entry_type))
        return entries
        
class PlayerControl(object):
    
    rbshell = None
    
    def __init__(self):
        try:
            self.__player = PlayerControl.rbshell.props.shell_player
            self.__queue = PlayerControl.rbshell.props.queue_source
            self.__library = PlayerControl.rbshell.props.library_source
            self.__dbaccess = DBAccess()
            self.__playlistManager = PlayerControl.rbshell.props.playlist_manager
        except NameError:
            print "You need to assign DBAccess.rbshell first!"
            raise
        
    def __loadPlaylists(self):
        self.__playlists= dict()
        for playlist in self.__playlistManager.get_playlists():
            self.__playlists[playlist.props.name] = playlist;
    
    def __play_entry(self, entry_id, source):
        self.__player.set_playing_source(source)
        self.__player.play_entry(self.__dbaccess.get_entry(entry_id), source)
        
    def __get_source_entries(self, source):
        entries = list()
        for row in source.get_query_model():
            entry = row[0]
            entry_id = entry.get_ulong(RB.RhythmDBPropType.ENTRY_ID)
            title = entry.get_string(RB.RhythmDBPropType.ARTIST) + " - " + entry.get_string(RB.RhythmDBPropType.TITLE)
            entries.append((entry_id, title))
        return entries
        
    def play(self):
        self.__player.play()
        
    def play_entry(self, entry_id):
        self.__play_entry(entry_id, self.__library)
        
    def play_entry_from_queue(self, entry_id):
        self.__play_entry(entry_id, self.__queue)
        
    def play_entry_from_playlist(self, entry_id, playlist):
        self.__loadPlaylists()
        if (self.__playlists.has_key(playlist)):
            self.__play_entry(entry_id, self.__playlists[playlist])
        
    def add_entry_to_queue(self, entry_id):
        self.__queue.add_entry(self.__dbaccess.get_entry(entry_id), -1)
        
    def stop(self):
        self.__player.stop()
        
    def pause(self):
        self.__player.pause()
    
    def has_next(self):
        return self.__player.props.has_next
    
    def has_prev(self):
        return self.__player.props.has_prev
    
    def next(self):
        try:
            self.__player.do_next()
        except:
            pass
        
    def previous(self):
        try:
            self.__player.do_previous()
        except:
            pass
        
    def seek(self, position):
        if self.has_prev():
            self.__player.seek(position);
        
    def is_playing(self):
        return self.__player.get_playing()[1]
    
    def get_playing_entry_id(self):
        entry = self.__player.get_playing_entry()
        if (entry is None):
            return -1
        return self.__player.get_playing_entry().get_ulong(RB.RhythmDBPropType.ENTRY_ID)
    
    def get_playing_entry_str(self):
        entry = self.__player.get_playing_entry()
        
        if (entry == None):
            return "-";
        
        title = entry.get_string(RB.RhythmDBPropType.TITLE)
        artist = entry.get_string(RB.RhythmDBPropType.ARTIST)
        return "[" + artist + "] - " + title;
    
    def get_playing_duration(self):
        if (not self.is_playing()):
            return 0
        return self.__player.get_playing_song_duration()
    
    def get_playing_time(self):
        print self.is_playing()
        if (not self.is_playing()):
            return 0
        return self.__player.get_playing_time()[1]
    
    def get_volume(self):
        return self.__player.get_volume()[1]
    
    def set_volume(self, volume):
        self.__player.set_volume(volume)
    
    def get_queue_entries(self):
        return self.__get_source_entries(self.__queue)
    
    def get_playlist_names(self):
        self.__loadPlaylists()
        return sorted(self.__playlists.keys())
    
    def get_playlist_entries(self, playlist):
        self.__loadPlaylists()
        if (not self.__playlists.has_key(playlist)):
            return None
        else:
            return self.__get_source_entries(self.__playlists[playlist])
        