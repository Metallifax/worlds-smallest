import os
import sys
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'ON') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# settings.py
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=('django.middleware.common.CommonMiddleware',
                        'django.middleware.csrf.CsrfViewMiddleware',
                        'django.middleware.clickjacking.XFrameOptionsMiddleware',
                        ),)

# In a production environment use these commands to set the ALLOWED_HOSTS

# -$ export DEBUG=off
# -$ export ALLOWED_HOSTS=localhost,example.com
# -$ python hello.py runserver

# To reset DEBUG to the default:

# -$ unset DEBUG

# views.py


def index(request):
    return HttpResponse('<h1><em>Hello world</em></h1>')


# urls.py
urlpatterns = (
    url(r'^$', index),
)

# WSGI app for Gateway Interface
application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
