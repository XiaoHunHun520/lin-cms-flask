from flask import Blueprint

def create_kami():
    bp_kami = Blueprint("kami", __name__)
    from app.api.kami.KamiList import kami_api

    bp_kami.register_blueprint(kami_api, url_prefix="/kamis")
    return bp_kami
