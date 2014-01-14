from fabric.api import local, sudo
from fabric.context_managers import shell_env
from fabric.decorators import hosts

import secrets

def run_pgsql(query, *args, **kwargs):
    psql_options = ""
    
    if 'host' in kwargs:
        psql_options += "--host=%s" % kwargs['host']
        del kwargs['host']
    
    psql_options += """ -c \\"%s\\" """ % query

    cmd = """psql %s """ % psql_options

    user = kwargs['user'] or "postgres"
    
    local("""sudo su %s -c "%s" """ % (user, cmd))

@hosts(['localhost',])
def install():
    local('pip install -r requirements/develop.txt')
    user = "dev"
    password = "dev"
    database = "dev"
    pg_user = "postgres"
    pg_host = "localhost"

    # create user
    run_pgsql("DROP USER IF EXISTS %s" % user, user=pg_user)
    run_pgsql("""CREATE USER %s WITH NOCREATEDB NOCREATEUSER ENCRYPTED """\
        """PASSWORD '%s' """ % (user, password), user=pg_user)

    # create database
    run_pgsql("DROP DATABASE IF EXISTS %s" % database, user=pg_user)
    run_pgsql("CREATE DATABASE %s WITH OWNER %s" % (database, user),\
        user=pg_user)

def deploy(location):
    if location == 'local':
        with shell_env(SECRET_KEY=secrets.SECRET_KEY):
            local("python revpapers/manage.py runserver 0.0.0.0:8000 " \
                "--settings=revpapers.settings.develop")


