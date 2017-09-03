from django.shortcuts import render

# Create your views here.

from django_pro.settings import DATABASES


def index(request):

    return render(request,'wechat/index.html',{'databases':DATABASES})
