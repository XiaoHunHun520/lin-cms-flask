from flask import Blueprint

pcapp_api = Blueprint("pcapp", __name__)

@pcapp_api.route("")
def get_pcapp():
    """
    获取id指定图书的信息
    """
    return 1