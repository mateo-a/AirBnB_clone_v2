#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import *
import time
import os
env.hosts = ['34.73.201.175', '35.172.183.33']


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

def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    file_ext = archive_path.split('/')[1]
    file_noext = file_ext.split('.')[0]
    releases_path = "/data/web_static/releases/{}/".format(file_noext)
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -zxvf /tmp/{} -C {}".format(file_ext, releases_path))
        run("rm -rf /tmp/{}".format(file_ext))
        run("mv -n {}/web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}/web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        return True
    except Exception:
        return False
