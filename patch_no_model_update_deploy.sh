#!/bin/sh
git pull
wait
cp -rf /home/ubuntu/eclweb/settings.py /home/ubuntu/eclweb/demo/demo/
wait
sudo service apache2 stop
wait
sudo service apache2 start