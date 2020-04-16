import jwt
import time
from django.shortcuts import render, redirect

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature, BadData
from common.func import render_json
from common import config


def creat_token(token_dict):
    token_dict['iat'] = time.time()

    headers = {
        'alg': "HS256"
    }

    jwt_token = jwt.encode(
        token_dict,
        config.secret_key,
        algorithm="HS256",
        headers=headers).decode("ascii")
    return jwt_token


def decrypt_token(jwt_token):
    data = None
    try:
        data = jwt.decode(jwt_token, config.secret_key, algorithms=['HS256'])
    except Exception as e:
        print(e)
    return data


def gen_token(token_dict):

    # 用来调用申请发送消息的token,有效期两个小时
    token_dict['iat'] = time.time()
    s = Serializer(secret_key=config.secret_key, salt=config.salt, expires_in=7200)
    access_token = s.dumps(token_dict)
    return access_token


def gen_long_token(rtoken):
    timestamp = time.time()

    # 用户信息的token,一个月更新一次
    rtoken['iat'] = time.time()
    s2 = Serializer(secret_key=config.secret_key, salt=config.salt, expires_in=60*60*24*30)
    reflush_token = s2.dumps(rtoken)
    # 保存到redis中
    return reflush_token


def auth(func):
    def inner(request, *args, **kwargs):
        # 用于验证token
        # token = request.META.get('HTTP_AUTHORIZATION')
        token = request.GET.get("token")
        print("token2 is %s", token)
        err, msg, data = auth_token(token)
        if err is not 202:
            return redirect('/')
        print(err)
        return func(request, *args, **kwargs)
    return inner


def auth_token(token):
    s = Serializer(secret_key=config.secret_key, salt=config.salt)
    try:
        data = s.loads(token)
    except SignatureExpired:
        # 超时, 建议重新申请
        msg = "token expired"
        err = 1402
        return err, msg, None
    except BadSignature as e:
        # 验证失败,检查是没有token还是错误
        encoded_payload = e.payload
        if encoded_payload is not None:
            try:
                s.load_payload(encoded_payload)
            except BadData:
                err = 1403
                msg = "token tampered"
                return err, msg, None
        err = 1402
        msg = "not token"
        return err, msg, None
    except:
        err = 1400
        msg = "unknown err"
        return err, msg, None

    if ('userid' not in data) or ('name' not in data):
        err = 1406
        msg = 'data err'
        return err, msg, None
    name = data.get('name')
    err = 202
    msg = '用户: {name}登录成功'.format(name=name)
    return err, msg, data