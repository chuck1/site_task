#!/bin/bash

temp=`mktemp`

echo "yes" > $temp

python manage.py flush < $temp

temp=`mktemp`

echo $USER > $temp

python manage.py createsuperuser --username $USER --email "$EMAIL"

