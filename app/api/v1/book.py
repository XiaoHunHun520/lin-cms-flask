"""
    a standard CRUD template of book
    通过 图书 来实现一套标准的 CRUD 功能，供学习
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from flask import Blueprint, g
from lin import DocResponse, Success, group_required, login_required, permission_meta

from lin.logger import Logger

from app.api import AuthorizationBearerSecurity, api
from app.api.v1.exception import BookNotFound
from app.api.v1.model.book import Book
from app.api.v1.schema import BookInSchema, BookOutSchema, BookQuerySearchSchema, BookSchemaList

book_api = Blueprint("book", __name__)

@book_api.route("/<int:id>")
@api.validate(
    resp=DocResponse(BookNotFound, r=BookOutSchema),
    tags=["图书"],
)
def get_book(id):
    """
    获取id指定图书的信息
    """
    book = Book.get(id=id)
    if book:
        return book
    raise BookNotFound


@book_api.route("")
@permission_meta(name="图书列表", module="图书")
@api.validate(
    resp=DocResponse(r=BookSchemaList),
    tags=["图书"],
)
def get_books():
    """
    获取图书列表
    """
    return Book.get(one=False)


@book_api.route("/search")
@api.validate(
    resp=DocResponse(r=BookSchemaList),
    tags=["图书"],
)
def search(query: BookQuerySearchSchema):
    """
    关键字搜索图书
    """
    return Book.query.filter(Book.title.like("%" + g.q + "%"), Book.is_deleted == False).all()


@book_api.route("", methods=["POST"])
# @login_required
@api.validate(
    resp=DocResponse(Success(12)),
    security=[AuthorizationBearerSecurity],
    tags=["图书"],
)
def create_book(json: BookInSchema):
    """
    创建图书
    """
    Book.create(**json.dict(), commit=True)
    return Success(12)
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_current_user,
    get_jwt_identity,
    verify_jwt_in_request,
)

@book_api.route("/<int:id>", methods=["PUT"])
@login_required
@api.validate(
    resp=DocResponse(Success(13)),
    security=[AuthorizationBearerSecurity],
    tags=["图书"],
)
def update_book(id, json: BookInSchema):
    """
    更新图书信息
    """
    user = get_current_user()
    print(user)
    book = Book.get(id=id)
    if book:
        book.update(
            id=id,
            **json.dict(),
            commit=True,
        )
        return Success(13)
    raise BookNotFound


@book_api.route("/<int:id>", methods=["DELETE"])
@permission_meta(name="删除图书", module="图书")
@Logger(template='{user.username}删除图书') # 推送的消息
@group_required
@api.validate(
    resp=DocResponse(BookNotFound, Success(14)),
    security=[AuthorizationBearerSecurity],
    tags=["图书"],
)
def delete_book(id):
    """
    传入id删除对应图书
    """
    book = Book.get(id=id)
    if book:
        # 删除图书，软删除
        book.delete(commit=True)
        return Success(14)
    raise BookNotFound


import ctypes
import inspect
import threading
import time
# 一，要在线程中执行的耗时函数
def Thread_Function(running):
    while running.is_set():
        print(running.is_set())
        time.sleep(1)

tt = None
tss = None

@book_api.route("/th")
# @permission_meta(name="删除图书", module="图书")
# @Logger(template='{user.username}删除图书') # 推送的消息
# @group_required
@api.validate(
    resp=DocResponse(BookNotFound),
    # security=[AuthorizationBearerSecurity],
    tags=["图书"],
)
def th():
    running = threading.Event()
    running.set()

    thread = threading.Thread(target=Thread_Function, args=(running,),name="thread-1")
    thread.start()
    print(thread.is_alive())
    print(thread.isDaemon())
    global tt
    global tss
    tt = running
    tss = thread
    print(tt)
    print(tss)
    print(thread.ident)
    return "ok"

@book_api.route("/s")
# @permission_meta(name="删除图书", module="图书")
# @Logger(template='{user.username}删除图书') # 推送的消息
# @group_required
@api.validate(
    resp=DocResponse(BookNotFound),
    # security=[AuthorizationBearerSecurity],
    tags=["图书"],
)
def s():

   # 四，判断线程是否已经销毁
    if tss != None and tss.is_alive():
        print("still running")
        print(tss)
        return "still running"
    else:
        print("completed")
        return "completed"
    # raise BookNotFound

@book_api.route("/ts")
# @permission_meta(name="删除图书", module="图书")
# @Logger(template='{user.username}删除图书') # 推送的消息
# @group_required
@api.validate(
    resp=DocResponse(BookNotFound),
    # security=[AuthorizationBearerSecurity],
    tags=["图书"],
)
def ts():

   # 四，判断线程是否已经销毁
    # tt.clear()
    # print(tt.clear())
    stop_thread(tss)
    return "退出成功"
    # raise BookNotFound

import inspect
import ctypes
def _async_raise(ttd, exctype):
    ttd = ctypes.c_long(ttd)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ttd, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ttd, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)