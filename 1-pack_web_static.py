#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import *
import time


def do_pack():
    """
    Function do_pack must return the archive path if the archive has been
    correctly generated. Otherwise, it should return None
    """
    the_time = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(the_time))
        return ("versions/web_static_{}.tgz".format(the_time))
    except:
        return None
