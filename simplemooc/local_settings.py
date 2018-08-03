DEBUG = True

TEMPLATE_DEBUG = True

# Allow all host headers
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
