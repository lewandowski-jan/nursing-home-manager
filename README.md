# nursing-home-manager

Nursing home manager program.

# Setup

## Global Requirements

1. Running locally oracle server 19c with newly created database
2. Installed instant_client
3. Installed python3
4. Installed pip
5. Installed git

## Windows

git clone https://github.com/iasiu/nursing-home-manager.git

cd nursing-home-manager

python -m venv env

.\env\Scripts\activate

pip install -r requirements.txt

cd webapp

copy con config.py

NAME="databasename"

USER="system"

PASSWORD="userpassword"

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
