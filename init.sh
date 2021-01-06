#!/bin/sh
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
gunicorn -b 0.0.0.0:8080 --workers=5 wsgi
sudo /etc/init.d/nginx restart

