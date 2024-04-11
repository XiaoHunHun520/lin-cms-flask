"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from lin import InfoCrud as Info
from lin import BaseCrud as Base
from sqlalchemy import Column, Integer, String


class KamiList(Info):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 密卡编号
    codeNumder = Column(String(128))
    # 卡密时间（已时间戳为计算）
    kamiTime = Column(Integer)
    # 0：未激活、1：已激活、2：已到期、3：已冻结
    status = Column(Integer)
    # 生效时间
    codeActivationTime = Column(String(128))
    # 无效时间
    codeInvalidTime = Column(String(128))
    # 卡密介绍
    introduce  = Column(String(512))
    
class KamiUid(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 卡密uid
    kamiid = Column(Integer)
    # 用户uid
    uid = Column(Integer)
    # 用户Nanm
    uidName = Column(String(64))
    # 网卡码
    networkCard = Column(String(64))

