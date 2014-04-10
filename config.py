# -*- coding: utf-8 -*-

# 手机快捷支付服务器异步通知地址
SECURITY_NOTIFY_URL = ''
# 手机网页支付服务器异步通知地址
WAP_NOTIFY_URL = ''
# 手机网页支付页面同步通知地址
WAP_CALL_BACK_URL = ''


# 支付宝网关
ALIPAY_GATEWAY = 'http://wappaygw.alipay.com/service/rest.htm?'

# 支付宝安全验证地址
ALIPAY_VERIFY_URL = 'https://mapi.alipay.com/gateway.do?service=notify_verify&'

# 支付宝合作身份证ID
PARTNER = ''

# 支付宝交易安全检验码
KEY = ''

# 支付宝商户私钥
PRIVATE_KEY = ""

# 支付宝公钥
ALIPAY_PUBLIC_KEY = ""

# 字符编码
INPUT_CHARSET = 'utf-8'

# 签名方式，可选0001(RSA), MD5
SIGN_TYPE = 'MD5'


# 支付宝账户
EMAIL = ''


TRADE_FINISHED = 'TRADE_FINISHED'

WAP_GATEWAY = 'http://wappaygw.alipay.com/service/rest.htm'


DEAL_TYPE = {
            'security':1,
            'wap':2,
            }

DEAL_STATUS = {
                'UNKNOWN':0,            # 防止支付宝新加状态..
                'WAIT_BUYER_PAY':1,     # 快捷支付创建交易后发
                'TRADE_CLOSED':2,       # 不会发, 以防万一
                'TRADE_SUCCESS':3,      # 不会发, 以防万一
                'TRADE_PENDING':4,      # 不会发, 以防万一
                'TRADE_FINISHED':5      # 快捷支付和网页支付付款成功后发
            }
