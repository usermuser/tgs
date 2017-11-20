# -*- coding:utf-8 -*-
print('local ')
print('      settings')
print('               loaded')

STATIC_ROOT=''   #override STATIC_ROOT variable to enable local path to static
print('empty STATIC_ROOT means that local_setting_rus loaded correctly')
#STATICFILES_DIRS must be equal STATIC_ROOT = /home/user/work/tgs/static
STATICFILES_DIRS = '/home/user/work/tgs/static','/home/tgs/work/tgs/static',
print('STATICFILES_DIRS=' , STATICFILES_DIRS)

''' << ABOUT STATICFILES_DIRS >>
https://stackoverflow.com/questions/12161271/can-i-make-staticfiles-dir-same-as-static-root-in-django-1-3

The STATICFILES_DIRS can contain other directories (not necessarily app directories) 
with static files and these static files will be collected into your STATIC_ROOT when 
you run collectstatic. These static files will then be served by your web server and 
they will be served from your STATIC_ROOT.

If you have files currently in your STATIC_ROOT that you wish to serve 
then you need to move these to a different directory and put that other 
directory in STATICFILES_DIRS. Your STATIC_ROOT directory should be empty 
and all static files should be collected into that directory (i.e., it should
 not already contain static files).
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
print('DATABASES variable set to use sqlite3')
