from flask import Blueprint

from app.api.v1.book import book_api


def create_v1():
    bp_v1 = Blueprint("v1", __name__)
    from app.api.v1.douyin import douyin_api

    bp_v1.register_blueprint(book_api, url_prefix="/book")
    bp_v1.register_blueprint(douyin_api, url_prefix="/tool")
    return bp_v1
