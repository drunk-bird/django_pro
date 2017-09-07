from yaml import load,dump



def load_conf(conf_key = None):
    f = open('wechat/config.ymal',encoding='utf-8')
    conf = load(f)
    f.close()
    return conf[conf_key] if conf_key else conf

#
# print(load_conf('welcome_text'))