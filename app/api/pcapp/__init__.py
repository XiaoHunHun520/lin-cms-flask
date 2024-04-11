from flask import Blueprint

# from app.api.blog.user import user_api


def create_pcapp():
    pcapp = Blueprint("pcapp", __name__)
    from app.api.pcapp.pcapp import pcapp_api
    

    pcapp.register_blueprint(pcapp_api, url_prefix="/pc")
    return pcapp
