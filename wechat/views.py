from django.shortcuts import render,HttpResponse
from wechat import models,config
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.messages import TextMessage



# Create your views here.

conf = WechatConf(**config.WECHATCONF)
wechat_obj = WechatBasic(conf=conf)

def auth(request):
    if request.method=='GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        if wechat_obj.check_signature(signature, timestamp, nonce):
            return HttpResponse(echostr)
        else:
            return HttpResponse('<h1>%s<h1>'%conf.token)
    if request.method=='POST':
        body_test = request.body
        wechat_obj.parse_data(body_test)
        if isinstance(wechat_obj.message,TextMessage):
            content = str(wechat_obj._WechatBasic__message.source)
            # content = "target openid:%s \n source openid:%s"%(wechat_obj.message.target,wechat_obj.message.source)
            response_test = wechat_obj.response_text(content, escape=False)
            return HttpResponse(response_test,content_type="application/xml")
        else:
            content ='error'
            response_test = wechat_obj.response_text(content, escape=False)
            return HttpResponse(response_test, content_type="application/xml")




def index(request):
    models.UserInfo.objects.create(name='arnol',password='123')
    DATABASES = models.UserInfo.objects.first()
    return render(request,'wechat/index.html',{'databases':DATABASES})

