#!/bin/sh
#pip3 install virtualenv
#virtualenv mystepik
#source mystepik/bin/activate
#python3 -m pip install --upgrade pip setuptools 
#python3 -m pip install -U Django
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo service nginx stop
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi
#git config --global user.name "Nanoku"
#git config --global user.email "nanokuvalda@gmail.com"
#django-admin startproject ask
#cd ask
#python manage.py startapp qa
#cp -f ~/web/views.py ~/web/ask/qa/views.py
#cp -f ~/web/urls.py ~/web/ask/ask/urls.py
#sudo gunicorn -c /home/box/web/gunicorn-django.conf --access-logfile acc.log --error-logfile err.log ask.wsgi:application
cd ~/web/
sudo gunicorn -w 4 -b 0.0.0.0:8080 hello:wsgi_application
#sudo cp -f gunicorn1.service /etc/systemd/system/gunicorn1.service
#sudo systemctl start gunicorn1
#sudo systemctl enable gunicorn1
#sudo cp -f gunicorn2.service /etc/systemd/system/gunicorn2.service
#sudo systemctl start gunicorn2
#sudo systemctl enable gunicorn2
