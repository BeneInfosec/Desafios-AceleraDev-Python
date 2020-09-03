from .settings import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}


# Heroku Statics Hack (não é muito recomendado para produção!!)
# https://devcenter.heroku.com/articles/django-assets

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
