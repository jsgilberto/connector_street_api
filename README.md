Connector Street API
====================

Connector Street backend. This API serves both the mobile app and the
admin web app.

![image](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter%0A%20%20:target:%20https://github.com/pydanny/cookiecutter-django/%0A%20%20:alt:%20Built%20with%20Cookiecutter%20Django)

![image](https://img.shields.io/badge/code%20style-black-000000.svg%0A%20%20:target:%20https://github.com/ambv/black%0A%20%20:alt:%20Black%20code%20style)

Settings
--------

Moved to
[settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

Basic Commands
--------------

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out
    the form. Once you submit it, you'll see a "Verify Your E-mail
    Address" page. Go to your console to see a simulated email
    verification message. Copy the link into your browser. Now the
    user's email should be verified and ready to go.
-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ docker-compose -f local.yml run django mypy connector_street_api

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ docker-compose -f local.yml run django coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ docker-compose -f local.yml run django pytest


### Celery

This app comes with Celery.

To run a celery worker:

``` {.sourceCode .bash}
cd connector_street_api
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where*
the celery commands are run. If you are in the same folder with
*manage.py*, you should be right.

### Email Server

In development, it is often nice to be able to see emails that are being
sent from your application. For that reason local SMTP server
[MailHog](https://github.com/mailhog/MailHog) with a web interface is
available as docker container.

Container mailhog will start automatically when you will run all docker
containers. Please check [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)
for more details how to start all containers.

With MailHog running, to view messages that are sent by your
application, open your browser and go to `http://127.0.0.1:8025`

Deployment
----------

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
