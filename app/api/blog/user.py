from flask import Blueprint, g
from lin import DocResponse,NotFound , Success, group_required, login_required, permission_meta

from app.api import AuthorizationBearerSecurity, api
from app.api.blog.model.user import BlogUser,generate_password,check_password
from app.api.blog.schema.user import LoginSchema,RegisterSchema


user_api = Blueprint("user", __name__)

@user_api.route("/register", methods=["POST"])
@api.validate(
    resp=DocResponse(Success()),
    security=[AuthorizationBearerSecurity],
    tags=["博客"],
)
def user_register(json: RegisterSchema):
    """
    用户注册
    """
    user = BlogUser.get(username=json.userName)
    print(user)
    if not user:
        BlogUser.create(
            username=json.userName,
            nickname=json.nickName,
            email=json.email,
            password=generate_password(json.password),
            signature="作者很懒，什么也没有留下！",
            state=0,
            commit=True,
        )
        return {"code": 200,"msg": "操作成功"}
    raise NotFound
from .exception.Jwt import generate_jwt_token,verify_jwt_token,check_token_blog
@user_api.route("/login", methods=["POST"])
@api.validate(
    resp=DocResponse(Success()),
    tags=["博客"],
)
def user_login(json: LoginSchema):
    """
    用户登录
    """
    user = BlogUser.get(username=json.userName)
    # from .exception.Jwt import Jwt_Token
    # from .exception.Jwt import generate_jwt_token,verify_jwt_token
    if user and check_password(user.password,json.password):
        token = generate_jwt_token(user.id)
        user = {
            "avatar": user.avatar_url,
            "email": user.email,
            "id": user.id,
            "nickName": user.nickname,
            "number": user.number,
            "state": user.state,
            "userName": user.username,
            "sex":user.sex,
            "signature":user.signature,
            "isAdmin": True,
        }
        # od = check_token(tokens)
        # print(token)
        # # print(verify_jwt_token(token))
        # # token = generate_jwt_token(user_id)
        # print(verify_jwt_token(user["id"], token))
        # token = "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjYTgyNDg1YmU1NDM0YjFkOGZlYmNlYzcwZjY4MjQ4MiIsInN1YiI6IjIiLCJpc3MiOiJ6aGl5aSIsImlhdCI6MTY0NzMzMjUxOSwiZXhwIjoxNjQ4NjI4NTE5fQ.Rir9HBL1NKJIkOUH1rzpESY77SnCnWWvhNkf4fK_Jxo"
        return {"code": 200,"msg": "操作成功","data":{"token":token,"userInfo":user}}
    raise NotFound
#     user = {
#     "code": 200,
#     "data": {
#         "token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjYTgyNDg1YmU1NDM0YjFkOGZlYmNlYzcwZjY4MjQ4MiIsInN1YiI6IjIiLCJpc3MiOiJ6aGl5aSIsImlhdCI6MTY0NzMzMjUxOSwiZXhwIjoxNjQ4NjI4NTE5fQ.Rir9HBL1NKJIkOUH1rzpESY77SnCnWWvhNkf4fK_Jxo",
#         "userInfo": {
#             "avatar": "https://img1.baidu.com/it/u=3257266420,40463730&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500",
#             "email": "shoko@qq.com",
#             "id": "2",
#             "nickName": "西宫硝子",
#             "sex": "1",
#             "signature": "我稀饭你",
#             "userName": "shoko"
#         }
#     },
#     "msg": "操作成功"
# }
    
    

@user_api.route("/adminInfo", methods=["GET"])
@api.validate(
    resp=DocResponse(Success()),
    tags=["博客"],
)
def get_adminlnfo():
    """
    获取管理员信息
    """
    data ={
    "code": 200,
    "data": {
        "avatar": "https://pic.aiyingli.com/wp-content/uploads/2017/04/2017-04-12_58edb0d7d47b4.gif",
        "email": "1319158137@qq.com",
        "id": "1",
        "nickName": "小企鹅",
        "sex": "0",
        "signature": "管理员",
        "userName": "admin"
    },
    "msg": "操作成功"
}
    return data

@user_api.route("/userInfo", methods=["GET"])
@api.validate(
    resp=DocResponse(Success()),
    tags=["博客"],
)
def get_userlnfo():
    """
    获取用户信息
    """
    data ={
    "code": 200,
    "data": {
        "avatar": "https://img1.baidu.com/it/u=3257266420,40463730&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500",
        "email": "shoko@qq.com",
        "id": "2",
        "nickName": "西宫硝子",
        "sex": "1",
        "signature": "我稀饭你",
        "userName": "shoko"
    },
    "msg": "操作成功"
}
    return data


@user_api.route("/logout", methods=["POST"])
@api.validate(
    resp=DocResponse(Success()),
    tags=["博客"],
)
def user_logout():
    """
    用户退出
    """
    data = {
    "code": 200,
    "msg": "操作成功"
    }
    return data