# pyCommerce
This is a basic django project with basic barebones structure

# You should already have the following installed
Python3
Pip3
# Steps
## Clone repo
git clone https://github.com/muathime/pyCommerce.git

## set and activate virtual env on your dev machine
python3 -m venv venv
source ./venv/bin/activate

## Install requirements
pip3 install -r requirements.txt

## Do migrations to create database schema
python3 manage.py makemigrations
python3 manage.py migrate

## Create new super user
python3 manage.py createsuperuser