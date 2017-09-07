


WECHATCONF = {  'token':'weixin',
                'appid':'wx2b33887e83cbbb1c',
                'encrypt_mode':'normal',
                  }


class Father(object):
    def __init__(self,message = None,name='ddd'):
        self.name = name
        self.message = message

    def get_name(self):
        print('name is father')


class Sub_class(Father):
    def __init__(self,message,name):
        super(Sub_class,self).__init__()

    def get(self):
        try:
            getattr(self,'get_name1')()
        except AttributeError :
            print('error func name')
        # print(self.get_name())


# a = Sub_class('sub_message','sub_test')
#
# print(a.get())


