from django.shortcuts import render,HttpResponse
from wechat import models,
from wechat_sdk import WechatConf
from wechat.modules.handle import Wechat_handle
from wechat.modules.config_handle import load_conf



# Create your views here.



def auth(request):
    conf = WechatConf(**load_conf('wechatconfig'))
    wechat_obj = Wechat_handle(conf=conf)

    if request.method=='GET':
        return HttpResponse(wechat_obj.get(request))

    if request.method=='POST':
        return HttpResponse(wechat_obj.post(request))




def index(request):
    models.UserInfo.objects.create(name='arnol',password='123')
    DATABASES = models.UserInfo.objects.first()
    return render(request,'wechat/index.html',{'databases':DATABASES})

