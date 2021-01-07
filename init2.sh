#!/bin/sh
git config --global user.name "Nanoku"
git config --global user.email "nanokuvalda@gmail.com"
django-admin startproject ask
cd ask
python manage.py startapp qa
cp -f ../views.py qa/views.py
cp -f ../urls.py ask/urls.py
