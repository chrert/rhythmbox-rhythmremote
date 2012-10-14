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

import os, sys, subprocess

__plugin_dir = os.path.expanduser("~/.local/share/rhythmbox/plugins/")
__plugin_name = "RhythmRemote"


def __cmd_exists(cmd):
    try:
        subprocess.call([cmd, '--version'])
    except OSError:
        print "%s not found on path" % myexec


def __install():
    pass

def __run():
    if (os.path.lexists(__plugin_dir + __plugin_name.lower())):
        os.unlink(__plugin_dir + __plugin_name.lower())
    os.symlink(os.path.abspath("."), __plugin_dir + __plugin_name.lower())
    os.execvp("rhythmbox", ["rhythmbox", "-D", __plugin_name.lower()])

def __check_dependencies():
    try:
        import bottle
    except:
        print("You need to install bottle (pip install bottle or apt-get install python-bottle or ...)")
        exit(1)
    
    try:
        subprocess.call(["rhythmbox", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError:
        print("Either Rhythmbox is not installed or not in your PATH environment variable.")
        print("Please install Rhythmbox properly to continue.")
        exit(1)
        
def __initialize_environment():
    if not os.path.exists(__plugin_dir):
        os.makedirs(__plugin_dir)
        print("Created Rhythmbox plugin-directory in: " + __plugin_dir)
        


if __name__ == "__main__":
    __check_dependencies()
    __initialize_environment()	

    if len(sys.argv) > 1 and sys.argv[1] == "install":
         __install()
    else:
         __run()
