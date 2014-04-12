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

# 支付宝交易安全检验码，用于MD5加密
KEY = ''

# 支付宝商户私钥，用于RSA加密
PRIVATE_KEY = ""

# 支付宝公钥，用于RSA验签
ALIPAY_PUBLIC_KEY = ""

# 字符编码
INPUT_CHARSET = 'utf-8'

# 签名方式，可选0001(RSA), MD5
SIGN_TYPE = 'MD5'

# 支付宝账户，所有订单款项都将打到这个账户。必须和支付宝分配的商户ID匹配。
EMAIL = ''

