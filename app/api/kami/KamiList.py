from flask import Blueprint, g
from lin import DocResponse,NotFound , Success, group_required, login_required, permission_meta
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_current_user,
    get_jwt_identity,
    verify_jwt_in_request,
)
from lin.logger import Logger

from flask import Blueprint, g
from app.api import AuthorizationBearerSecurity, api
from app.api.kami.exception.kami import KamiNotFound, KamiActivation,KamiUnbound,KamiNoSvailableNotFound
from app.api.kami.model.kami import KamiList,KamiUid
from app.api.kami.schema.kami import KamiaddSchema,KamicheckSchema,getKamilistSchema,updatekamistatusSchema,getKamiUserSchema
from app.util.kami import kami_tool, kami_tool_time

import time
import hashlib
import random


kami_api = Blueprint("Kami", __name__)

@kami_api.route("", methods=["GET"])
@permission_meta(name="查询所有卡密", module="卡密")
@group_required
@api.validate(
    resp=DocResponse(Success()),
    security=[AuthorizationBearerSecurity],
    tags=["卡密"],
    query=getKamilistSchema,
)
def get_kami():
    """
    获取卡密列表
    """
    kamis = KamiList.query.filter(KamiList.is_deleted == False,KamiList.status == 1).all()
    for i in kamis:
        check_time = kami_tool(i.codeActivationTime,i.codeInvalidTime)
        if check_time == False:
            i.update(id=i.id,status=2,commit=True)

    kamilist = KamiList.query.filter(
        KamiList.is_deleted == False).paginate(page=int(g.currentPage),
        per_page=int(g.pageSize),
        error_out=False, max_per_page=None)
    user = kamilist.items
    # codeNumdercode = {
    #     "id":user.id,
    #     "codeNumder":user.codeNumder,
    #     "status":user.status,
    #     "introduce":user.introduce
    # }
    data = {
        "items":user,
        "paginate":kamilist.page,
        "total":kamilist.total
    }
    return data

@kami_api.route("/kamiuser", methods=["GET"])
@permission_meta(name="查询用户归属卡密", module="卡密")
@group_required
@api.validate(
    resp=DocResponse(Success(25)),
    security=[AuthorizationBearerSecurity],
    tags=["卡密"],
    query=getKamiUserSchema)
def kami_user():
    """查询用户归属卡密"""
    codeNumder =  KamiUid.get(kamiid=g.codeNumderid)
    if codeNumder:
        # codeNumder_dict = {
        #     "id":codeNumder.id,
        #     "uidName":codeNumder.uidName,
        #     "networkCard":codeNumder.networkCard,
        # }
        return codeNumder
    raise KamiUnbound

# 验证卡密
@kami_api.route("/check", methods=["POST"])
@login_required
@api.validate(
    resp=DocResponse(Success(25)),
    security=[AuthorizationBearerSecurity],
    tags=["卡密"])
def check_kami(json: KamicheckSchema):
    """验证卡密"""
    user = get_current_user()
    checks = KamiList.query.filter_by(codeNumder=json.codeNumder, is_deleted=False).first()
    if checks:
        checkid = KamiUid.get(kamiid=checks.id)
        if not checkid:
            raise KamiNotFound
        if checks.status == 1 and user.id == checkid.uid and checkid.networkCard == json.networkCard:
            check_time = kami_tool(checks.codeActivationTime,checks.codeInvalidTime)
            if check_time:
                return {"Expiration_time":check_time}
            else:
                checks.update(id=checks.id,status=2,commit=True)
                # 卡密已到期 返回不存在
                raise KamiNotFound
    raise KamiNoSvailableNotFound

# 激活卡密
@kami_api.route("/start", methods=["POST"])
@login_required
@api.validate(
    resp=DocResponse(Success()),
    security=[AuthorizationBearerSecurity],
    tags=["卡密"]
)
def start_kami(json: KamicheckSchema):
    """激活卡密"""
    user = get_current_user()
    checks = KamiList.query.filter_by(codeNumder=json.codeNumder, is_deleted=False).first()
    if checks:
        if checks.status == 0:
            start_time = kami_tool_time(checks.kamiTime)
            checks.update(id=checks.id,
            status=1,
            codeActivationTime=start_time[0],
            codeInvalidTime=start_time[1],
            commit=True)
            KamiUid.create(
                uid=user.id,
                kamiid=checks.id,
                uidName=user.username,
                networkCard=json.networkCard,
                commit=True)
            return Success(26)
    raise KamiNotFound

# 添加卡密
@kami_api.route("/add", methods=["POST"])
@permission_meta(name="添加卡密", module="卡密")
@group_required
@api.validate(
    resp=DocResponse(Success(20)),
    security=[AuthorizationBearerSecurity],
    tags=["卡密"],
)
def create_kami(json: KamiaddSchema):
    """创建卡密"""
    times = str(time.time())
    rd = random.choice("luofengcheng")
    kami_add = str(times + rd)
    sha1 = hashlib.sha1(kami_add.encode("utf-8")).hexdigest()
    sha1s = hashlib.sha1(sha1.encode("utf-8")).hexdigest()
    status = 0
    KamiList.create(
        codeNumder=sha1s,
        status=status,
        kamiTime = json.kamitime * 60 * 60 * 24,
        introduce = json.introduce,
        commit=True)

    return Success(20)

# 更新卡密状态
@kami_api.route("/<int:id>", methods=["PUT"])
@api.validate(
    resp=DocResponse(),
    security=[AuthorizationBearerSecurity],
    tags=["卡密"]
)
def update_kami_status(id: int,json: updatekamistatusSchema):
    """
    传入id更新卡密状态
    """
    kami = KamiList.get(id=id)
    print(kami)
    if kami:
        # 更新卡密状态
        kami.update(id=kami.id,status=json.status,commit=True)
        return Success(23,"更新卡密状态成功")
    raise NotFound(10020)

@kami_api.route("/<int:id>", methods=["DELETE"])
@permission_meta(name="删除卡密", module="卡密")
@Logger(template='{user.username}删除一张卡密') # 推送的消息
@group_required
@api.validate(
    resp=DocResponse(Success),
    security=[AuthorizationBearerSecurity],
    tags=["卡密"]
)
def delete_kami(id: int):
    """
    传入id删除对应卡密
    """
    kami = KamiList.get(id=id)
    print(kami)
    if kami:
    #     # 删除卡密，软删除
    #     kami.delete(commit=True)
        return Success(29,"删除卡密成功")
    raise NotFound(10020)

