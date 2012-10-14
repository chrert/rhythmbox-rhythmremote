# RhythmRemote

The goal of this project is to create a fully functional mobile web-interface for Rhythmbox.
It's implemented as an Rhythmbox plugin written in python. The plugin starts a local webserver on 0.0.0.0:8001 (or localhost), which handles the requests of the browser.

## Screenshots
![Search interprets](RhythmRemote/screenshots/interprets.png "Search interprets")

![Play track](RhythmRemote/screenshots/play.png "Play tracks")

## Prerequisites

* Rhythmbox 2.96+
* Bottle (python module)
* Modern Webrowser (HTML5 enabled)

The plugin is currently tested with Rhythmbox 2.96 and 2.97 on Debian testing (wheezy) and Firefox 10+ only.

## Functionality

### What works

* Browsing the music-database in a very strict way (Interprets -> Albums -> Tracks)
* Choose single title to play
* Play/Pause/Stop
* Previous/Next (if a playlist was chosen inside Rhythmbox)
* Adjust Volume
* Seek

### Feature plans

* Playlist Support
* Queue Support
* Enhanced search functionality (just like in Rhythmbox)
* Cover-Art
* Localizations
* Almost feature of standard Rhythmbox
