from django.shortcuts import render,HttpResponse
from wechat import models
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic

conf = WechatConf(
    token='weixin',
    appid='wx2b33887e83cbbb1c',
)

wechat_obj = WechatBasic(conf=conf)


# Create your views here.



def index(request):
    models.UserInfo.objects.create(name='arnol',password='123')
    DATABASES = models.UserInfo.objects.first()
    return render(request,'wechat/index.html',{'databases':DATABASES})


def auth(request):
    if request.method=='GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        if wechat_obj.check_signature(signature, timestamp, nonce):
            return HttpResponse(echostr)
        else:
            return HttpResponse('<h1>error<h1>')


