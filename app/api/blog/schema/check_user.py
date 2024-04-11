from app import create_app
from functools import wraps
from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# app = create_app()

# app.config["JWT_SECRET_KEY"] = "super-secret"  
# # 设置普通JWT过期时间
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
# # 设置刷新JWT过期时间
# app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
# jwt = JWTManager(app)


def login_required_no(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        # _check_is_active(current_user=get_current_user())
        userInfo = get_jwt_identity()
        if userInfo:
            return fn(*args, **kwargs)
        else:
            return userInfo

    return wrapper

def get_tokens_no(user):
    SCOPE = "lin"
    identity = dict(uid=0,scope=SCOPE)
    identity["uid"] = user
    access_token = create_access_token(identity)
    refresh_token = create_refresh_token(identity)
    return access_token, refresh_token

# @app.route("/login", methods=["POST"])
# def login():
#     access_token = create_access_token(identity="example_user")
#     refresh_token = create_refresh_token(identity="example_user")
#     return {"access_token":access_token, "refresh_token":refresh_token}


# # 使用刷新JWT来获取普通JWT
# @app.route("/refresh", methods=["POST"])
# @jwt_required(refresh=True)
# def refresh():
#     identity = get_jwt_identity()
#     access_token = create_access_token(identity=identity)
#     return jsonify(access_token=access_token)


# @app.route("/protected", methods=["GET"])
# @jwt_required()
# def protected():
#     return jsonify(foo="bar")