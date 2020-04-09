#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

loc="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n"

sudo sed -i "38i $loc" /etc/nginx/sites-available/default
service nginx restart
