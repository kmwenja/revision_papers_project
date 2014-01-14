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

    # drop database if exists
    run_pgsql("DROP DATABASE IF EXISTS %s" % database, user=pg_user)

    # drop user if exists
    run_pgsql("DROP USER IF EXISTS %s" % user, user=pg_user)

    # create user
    run_pgsql("""CREATE USER %s WITH NOCREATEDB NOCREATEUSER ENCRYPTED """\
        """PASSWORD '%s' """ % (user, password), user=pg_user)

    # create database
    run_pgsql("CREATE DATABASE %s WITH OWNER %s" % (database, user),\
        user=pg_user)

def manage(cmd, options="", cmd_options=""):
    local("python revpapers/manage.py %s %s %s" % (options, cmd, cmd_options))

def deploy(location):
    if location == 'local':
        settings = "--settings=revpapers.settings.develop"
        with shell_env(SECRET_KEY=secrets.SECRET_KEY):
            manage("syncdb", cmd_options=settings)
            manage("migrate", cmd_options=settings)
            manage("runserver",cmd_options="0.0.0.0:8000 "+ settings)


