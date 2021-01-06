#!/bin/sh
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo nginx -c /etc/nginx/sites-enabled/test.conf
git config --global user.name "Nanoku"
git config --global user.email "nanokuvalda@gmail.com"
gunicorn -w 4 -b 0.0.0.0:8080 hello:wsgi_application

