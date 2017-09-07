
WECHATCONF = {  'token':'weixin',
                'appid':'wx2b33887e83cbbb1c',
                'encrypt_mode':'normal',
                  }

WELCOME_TEXT = "感谢关注[愉快]\n我是星喵大人[调皮]\n\n"

from yaml import load, dump


w = open('config.ymal',encoding='utf-8')
print(load(w)['welcome_test'])

