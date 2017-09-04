from django.shortcuts import render
from wechat import models

# Create your views here.



def index(request):
    models.UserInfo.objects.create(name='arnol',password='123')
    DATABASES = models.UserInfo.objects.first()
    return render(request,'wechat/index.html',{'databases':DATABASES})
