
import time

import jwt
from jwt import exceptions
import functools
from flask import request

JWT_TOKEN_EXPIRE_TIME = 3600 * 2  # token有效时间 2小时
JWT_SECRET = 'abc'   # 加解密密钥
JWT_ALGORITHM = 'HS256'  # 加解密算法


def generate_jwt_token(user_id: int)->str:
    """根据用户id生成token"""
    print(user_id)
    payload = {'user_id': user_id, 'exp': int(time.time()) + JWT_TOKEN_EXPIRE_TIME}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token
    
    
def verify_jwt_token( token: str)->bool:
    """验证用户token"""
    payload = None
    msg = None
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except exceptions.ExpiredSignatureError:
        msg = "token已失效"
    except jwt.DecodeError:
        msg = "token认证失败"
    except jwt.InvalidTokenError:
        msg = "非法token"
    # if not payload:
    #     return False,msg
    return (payload, msg)

def check_token_blog(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. 获取用户请求头中的 用户名 信息
        token = request.headers.get("token")
        if not all([token]):
            return {"code":404, "message":"token参数不完整"}
        tokens = verify_jwt_token(token)
        print(tokens[0])
        if tokens[0]:
            return func(*args, **kwargs)
        else:
            return {"code":404, "message":tokens[1]}
    return wrapper