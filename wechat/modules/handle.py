from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.messages import TextMessage


class wechat_handle(WechatBasic):
    def __init__(self,conf):
        super(wechat_handle,self).__init__(conf=conf)


    def get(self,request):
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        if self.check_signature(signature, timestamp, nonce):
            return echostr
        else:
            return 'error'