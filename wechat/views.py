from django.shortcuts import render

# Create your views here.

from django_pro.settings import DATABASES
import os


def index(request):
    try:
        DATABASES = {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.getenv('MYSQL_DATABASE'),
                'USER': os.getenv('MYSQL_USER'),
                'PASSWORD': os.getenv('MYSQL_PASSWORD'),
                'HOST': os.getenv('MYSQL_SERVICE_HOST'),
                'PORT': os.getenv('MYSQL_SERVICE_PORT'),

            }
    except Exception as error:
        print(error)
        DATABASES = {'ENGINE': 'django.db.backends.mysql',}
    return render(request,'wechat/index.html',{'databases':DATABASES})
