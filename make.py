import os, sys

__plugin_dir = os.path.expanduser("~/.local/share/rhythmbox/plugins/")
__plugin_name = "Rhythmwebfork"


def __install():
    pass

def __run():
    if (os.path.lexists(__plugin_dir + __plugin_name.lower())):
        os.unlink(__plugin_dir + __plugin_name.lower())
    os.symlink(os.path.abspath("."), __plugin_dir + __plugin_name.lower())
    os.execvp("rhythmbox", ["rhythmbox", "-D", __plugin_name.lower()])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "install":
         __install()
    else:
         __run()