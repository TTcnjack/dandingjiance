import jwt
import time

import config
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature, BadData


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


def gen_token(token_dict, rtoken):

    # 用来调用申请发送消息的token,有效期两个小时
    token_dict['iat'] = time.time()
    s = Serializer(secret_key=config.secret_key, salt=config.salt, expires_in=7200)
    access_token = s.dumps(token_dict)
    timestamp = time.time()

    # 用户信息的token,一个月更新一次
    rtoken['iat'] = time.time()
    s2 = Serializer(secret_key=config.secret_key, salt=config.salt, expires_in=60*60*24*30)
    reflush_token = s2.dumps(rtoken)
    # 保存到redis中
    return access_token, reflush_token



def tokenAuth(token):
    # 用于验证token
    s = Serializer(secret_key=config.secret_key, salt=config.salt)
    try:
        data = s.loads(token)
    except SignatureExpired:
        # 超时, 建议重新申请
        msg = "token expired"

    except BadSignature as e:
        # 验证失败,检查是没有token还是错误
        encoded_payload = e.payload
        if encoded_payload is not None:
            try:
                s.load_payload(encoded_payload)
            except BadData:
                msg = "token tampered"

        msg = "not token"
    except:
        msg = "unknown err"

    return