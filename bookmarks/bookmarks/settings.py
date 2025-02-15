"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 3.0.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aup-0vz_k-sd)uqlhu%%vv=i8e-xa(i8b7icoh3ni0i9uj%kc$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',  # why this here you will find the reason at the comment below
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',  # for social authentication
    'django_extensions',
    'images.apps.ImagesConfig',
    'easy_thumbnails',  # when you have a large image it will make it load faster
    'actions.apps.ActionsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # included by default to make notifications for your users
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmarks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmarks.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# variables for login
LOGIN_REDIRECT_URL = 'dashboard'  # Tells Django which URL to redirect the user to after a successful login if no
# next parameter is present in the request
LOGIN_URL = 'login'  # The URL to redirect the user to log in (for example, views using the login_required decorator)
LOGOUT_URL = 'logout'  # The URL to redirect the user to log out

'''
If you see the logged out page of the Django administration site 
instead of your own logged out page, check the INSTALLED_APPS
setting of your project and make sure that django.contrib.
admin comes after the account application. Both templates are 
located in the same relative path, and the Django template loader 
will use the first one it finds.
'''

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_URL = '/media/'  # for allowing the users to upload files (photos, videos)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

'''
from django.contrib import messages
messages.error(request, 'Something went wrong') 
# to display notification to the user there are also a built_in notifications

• success(): Success messages to be displayed after an action has been successful
• info(): Informational messages
• warning(): Something has not yet failed but may fail imminently
• error(): An action was not successful or something failed
• debug(): Debug messages that will be removed or ignored in a production environment

'''

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',  # to enable facebook authentication
    # 'social_core.backends.twitter.TwitterOAuth',  # to enable twitter authentication
    'social_core.backends.google.GoogleOAuth2',  # to enable google authentication

]

# for facebook api
SOCIAL_AUTH_FACEBOOK_KEY = '232236808845173'  # APP ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'e1cb56484b0be66434f3aa2fe278296c'  # FACEBOOK APP SECRET

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']  # you asking the facebook to get user email

# for google api

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '530962793610-0lpjp3cbe9f64un80ns31tp4dpncdlt0.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'JgMwj7uZgo0Hgl5LWiJGd-_X'

'''
to make social authentication in django do the following steps:
1- pip install social-auth-app-django==3.1.0
2- add 'social_django' to installed apps
3- run python manage.py migrate
# i will make it for google, twitter and facebook
4- add 
path('social-auth/', include('social_django.urls', namespace='social')), 
to the main urls file
5- modify hosts file and add the following line (127.0.0.1 mysite.com) without hashtag
    because social authentication needs domain name.
6- assign ['mysite.com', 'localhost', '127.0.0.1'] to allowed_hosts 

# Some of the social authentication methods you are going to use require an HTTPS 
# connection.

# making https.
7- pip install django-extensions==2.2.5
8- pip install werkzeug==0.16.0
9- pip install pyOpenSSL==19.0.0
10- add 'django_extensions', to the installed_apps
11- run the server using
        python manage.py runserver_plus --cert-file cert.crt
    not
        python manage.py runserver


# You can now serve your site through HTTPS during development in order to test 
# social authentication with Facebook, Twitter, and Google.
# for real world there are a different method to do real https.
12 - 159 to 164 for facebook api
13- twitter bad services denied me from doing that
'''

# to make https faster
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

'''
A bookmarklet is a bookmark stored in a web browser that contains JavaScript 
code to extend the browser's functionality. When you click on the bookmark, the 
JavaScript code is executed on the website being displayed in the browser. This is 
very useful for building tools that interact with other websites.
Some online services, such as Pinterest, implement their own bookmarklets to let 
users share content from other sites onto their platform.


'''

from django.urls import reverse_lazy

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail',
                                        args=[u.username])
}
