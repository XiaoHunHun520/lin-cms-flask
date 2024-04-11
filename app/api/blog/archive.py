from flask import Blueprint, g
from lin import DocResponse,NotFound , Success, group_required, login_required, permission_meta

from app.api import AuthorizationBearerSecurity, api
from app.api.blog.model.user import BlogUser, generate_password,check_password
from app.api.blog.schema.user import LoginSchema,RegisterSchema,LoginTokenSchema


archive_api = Blueprint("archive", __name__)

@archive_api.route("/archiveList", methods=["GET"])
# @permission_meta(name="注册", module="非系统用户")
# @login_required_no
@api.validate(
    resp=DocResponse(Success()),
    # security=[AuthorizationBearerSecurity],
    tags=["博客"],
)
def get_archive_archiveList():
    """
    获取归档列表
    """
    data = {
    "code": 200,
    "data": {
        "rows": [
            {
                "articles": [
                    {
                        "createTime": "2022-03-14 00:27:57",
                        "id": "1",
                        "thumbnail": "https://i.niupic.com/images/2022/03/14/9Ws2.png",
                        "title": "如何在 pyqt 中解决国际化 tr() 函数不管用的问题",
                        "viewCount": "6"
                    },
                    {
                        "createTime": "2022-03-13 23:59:15",
                        "id": "2",
                        "thumbnail": "https://i.niupic.com/images/2022/03/12/9Wma.png ",
                        "title": "如何在 Vue3 中处理 img 标签图片加载错误的问题",
                        "viewCount": "6"
                    },
                    {
                        "createTime": "2022-02-12 22:32:45",
                        "id": "3",
                        "thumbnail": "https://i.niupic.com/images/2022/03/12/9Wme.jpg",
                        "title": "对 python 中 @property 装饰器的一点思考",
                        "viewCount": "34"
                    },
                    {
                        "createTime": "2022-01-12 21:16:07",
                        "id": "4",
                        "thumbnail": "https://i.niupic.com/images/2022/03/11/9Wl7.jpg",
                        "title": "测试 Kila Kila Blog 的博客样式",
                        "viewCount": "73"
                    }
                ],
                "year": 2022
            },
            {
                "articles": [
                    {
                        "createTime": "2021-12-13 13:24:53",
                        "id": "5",
                        "thumbnail": "https://i.niupic.com/images/2022/03/11/9Wl4.jpg",
                        "title": "如何在 IDEA 中配置 Easy Code 的 MybatisPlus 实体类模板",
                        "viewCount": "8"
                    },
                    {
                        "createTime": "2021-11-09 00:30:14",
                        "id": "6",
                        "thumbnail": "https://i.niupic.com/images/2022/03/11/9Wl0.png ",
                        "title": "如何处理 SSD 神经网络在小目标检测数据集上 mAP 和置信度较低的问题",
                        "viewCount": "2"
                    }
                ],
                "year": 2021
            }
        ],
        "total": "6"
    },
    "msg": "操作成功"
}
    return data

@archive_api.route("/archiveCountList", methods=["GET"])
@api.validate(
    resp=DocResponse(Success()),
    tags=["博客"],
)
# @login_required_no
def user_archiveCountList():
    """
    获取归档及其包含的文章数量
    """
    data = {
    "code": 200,
    "data": {
        "rows": [
            {
                "count": 2,
                "date": "2022/3"
            },
            {
                "count": 1,
                "date": "2022/2"
            },
            {
                "count": 1,
                "date": "2022/1"
            },
            {
                "count": 1,
                "date": "2021/12"
            },
            {
                "count": 1,
                "date": "2021/11"
            }
        ],
        "total": "5"
    },
    "msg": "操作成功"
}
    
    return data
    