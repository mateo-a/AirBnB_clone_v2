#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives, using the funtion do_clean
"""
from fabric.api import *
env.hosts = ['34.73.201.175', '35.172.183.33']


def do_clean(number=0):
    """
    deletes out-of-date archives, using the function do_clean
    """
    number = int(number)
    if number == 0:
        number = 2
    else:
        number = number + 1
    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs rm -rf'.format(number))
    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number))
