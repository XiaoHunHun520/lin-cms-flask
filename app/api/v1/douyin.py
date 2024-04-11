# -- coding: utf-8 --**
"""
    a standard CRUD template of book
    通过 图书 来实现一套标准的 CRUD 功能，供学习
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from flask import Blueprint, g
from lin import DocResponse,NotFound , Success, group_required, login_required, permission_meta
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_current_user,
    get_jwt_identity,
    verify_jwt_in_request,
)

from lin import (
    DocResponse,
    Duplicated,
    Failed,
    Log,
    Logger,
    NotFound,
    ParameterError,
    Success,
    admin_required,
    db,
    get_tokens,
    login_required,
    manager,
    permission_meta,
)

from lin.logger import Logger

from app.api import AuthorizationBearerSecurity, api
from app.api.v1.exception import BookNotFound
from app.api.v1.model.tooldy import ToolDy
from app.api.v1.schema.tooldy import DyInSchema

import re
import requests
import argparse
from flask import *

def work(share_link):

    url = 1
    # print(url)
    # key_type, key = tk.getKey(url)
    # print(key_type, key)
    # if key_type == "aweme":
    #     datanew, dataraw = tk.getAwemeInfo(key)
    # elif key_type == "live":
    #     datanew = tk.getLiveInfo(key, option=False)
    # elif key_type == "user":
    #     datanew = tk.getUserInfo(key)
    return url


douyin_api = Blueprint("tool", __name__)

@douyin_api.route("/douyin", methods=["POST"])
# @login_required
@api.validate(
    resp=DocResponse(),
    security=[AuthorizationBearerSecurity],
    tags=["抖音"]
)
def get_dy(json: DyInSchema):
    """
    抖音去水印
    """
    res = work(json.url)
    return {"数据":0}
    # if request.method == "GET":
    #     res = run(json.url)
    #     return res
    # elif request.method == "POST":
    #     res = run(json.url)
    #     return res
    # else:
    #     return "只接受POST与GET请求"

        
import time
@douyin_api.route("/files", methods=["GET"])
# @login_required
@api.validate(
    resp=DocResponse(),
    security=[AuthorizationBearerSecurity],
    tags=["抖音"]
)
def get_dys():
    n = 0
    start = time.perf_counter()
    int = get_int(n)
    end = time.perf_counter()
    return end - start,int
    
def get_int(x):
    for k in range(100000000):
        for j in range(10000000):
            x += 2 - 1
    return x