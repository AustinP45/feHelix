
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

##### Needs changed #####
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite',
		'USER': 'mysiteuser',
		'PASSWORD': 'mysiteSE2015',
		'HOST': '127.0.0.1',
		'PORT': '5432',
    }
}