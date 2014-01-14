from fabric.api import local
from fabric.context_managers import shell_env

import secrets

def install():
    local('pip install -r requirements/develop.txt')

def deploy(location):
    if location == 'local':
        with shell_env(SECRET_KEY=secrets.SECRET_KEY):
            local("python revpapers/manage.py runserver 0.0.0.0:8000 --settings=revpapers.settings.develop")


