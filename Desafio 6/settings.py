import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'ii3ojilqw2q-m@%fnfgjx2jyq8!8#ig3q=a$nehdns#b#02n(a'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'api.apps.ApiConfig',
    'rest_framework',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'python-10/db.sqlite3'),
    }
}

ROOT_URLCONF = 'urls'

