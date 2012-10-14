# RhythmRemote

The goal of this project is to create a fully functional mobile web-interface for Rhythmbox.
It's implemented as an Rhythmbox plugin written in python. The plugin starts a local webserver on 0.0.0.0:8001 (or localhost), which handles the requests of the browser.

## Screenshots
![Search interprets](https://raw.github.com/erti/rhythmbox-rhythmremote/master/screenshots/interprets.png "Search interprets")

![Play track](https://raw.github.com/erti/rhythmbox-rhythmremote/master/screenshots/play.png "Play tracks")

## Prerequisites

* Rhythmbox 2.96+
* Bottle (python module)
* Modern Webrowser (HTML5 enabled)

The plugin is currently tested with Rhythmbox 2.96 and 2.97 on Debian testing (wheezy) and Firefox 10+ only.

## Installation

Simply run the python script make.py without arguments. The script will check the dependencies, create the plugin folder
and symlink the plugin into that folder. Additionally it will start rhythmbox without debug output enabled for the plugin.

If you want to install the plugin, run:

```bash
python make.py install
```

This will copy the plugin-files to ~/.local/share/rhythmbox/plugins

The repository also includes an Eclipse-Project (with PyDev Extension) with configured Debug/Run configurations. 

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
