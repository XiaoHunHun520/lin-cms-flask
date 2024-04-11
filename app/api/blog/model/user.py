"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from lin import InfoCrud as Base
from sqlalchemy import Column, Integer, String

from werkzeug.security import generate_password_hash, check_password_hash


class BlogUser(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 用户名
    username = Column(String(64))
    # 密码
    password = Column(String(256))
    # 昵称
    nickname = Column(String(24))
    # 状态0 1
    state = Column(Integer)
    # 邮箱
    email = Column(String(128))
    # 手机号
    number = Column(String(128))
    # 用户头像
    avatar_url  = Column(String(256))
    # 性格签名
    signature = Column(String(64))
    # 性别
    sex = Column(Integer)
    
# 加密函数
def generate_password(value):
    return generate_password_hash(value)

# 密码校验装饰器
def check_password(pwd,password):
    return check_password_hash(pwd,password)