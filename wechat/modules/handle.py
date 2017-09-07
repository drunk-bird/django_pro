from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.messages import TextMessage


class Wechat_handle(WechatBasic):
    def __init__(self,conf):
        super(Wechat_handle,self).__init__(conf=conf)


    def get(self,request):
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        if self.check_signature(signature, timestamp, nonce):
            return echostr
        else:
            return 'error'

    def post(self,request):
        body_test = request.body
        self.parse_data(body_test)
        message = self.get_message()
        resp_func_name = '%s_resp'%message.type
        try :
            return getattr(self,resp_func_name)(message)
        except AttributeError:
            return self.error_resp(message)



    def text_resp(self,message):
        content = "target openid:%s \n source openid:%s" % (message.target,message.source)
        return self.response_text(content)



    def image_resp(self,message):
        pass

    def shortvideo_resp(self,message):
        pass

    def link_resp(self,message):
        pass

    def location_resp(self,message):
        pass

    def voice_resp(self,message):
        pass

    def subscribe_resp(self,message):
        pass

    def error_resp(self,message):
        content = 'wrong send type'
        return self.response_text(content)

