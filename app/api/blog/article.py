from flask import Blueprint, g
from lin import DocResponse,NotFound , Success, group_required, login_required, permission_meta

from app.api import AuthorizationBearerSecurity, api
from app.api.blog.schema.user import LoginSchema,RegisterSchema,LoginTokenSchema
from app.api.blog.schema.check_user import login_required_no,get_tokens_no

article_api = Blueprint("article", __name__)

@article_api.route("/hotArticleList", methods=["GET"])
@api.validate(
    resp=DocResponse(Success()),
    # security=[AuthorizationBearerSecurity],
    tags=["博客"],
)
def get_article_hotArticleList():
    """
    获取热度前十的文章
    """
    ho = {
    "code": 200,
    "data": [
        {
            "createTime": "2022-01-12 21:16:07",
            "id": "4",
            "thumbnail": "https://i.niupic.com/images/2022/03/11/9Wl7.jpg",
            "title": "测试 Kila Kila Blog 的博客样式",
            "viewCount": "72"
        },
        {
            "createTime": "2022-02-12 22:32:45",
            "id": "3",
            "thumbnail": "https://i.niupic.com/images/2022/03/12/9Wme.jpg",
            "title": "对 python 中 @property 装饰器的一点思考",
            "viewCount": "34"
        },
        {
            "createTime": "2021-12-13 13:24:53",
            "id": "5",
            "thumbnail": "https://i.niupic.com/images/2022/03/11/9Wl4.jpg",
            "title": "如何在 IDEA 中配置 Easy Code 的 MybatisPlus 实体类模板",
            "viewCount": "8"
        },
        {
            "createTime": "2022-03-13 23:59:15",
            "id": "2",
            "thumbnail": "https://i.niupic.com/images/2022/03/12/9Wma.png ",
            "title": "如何在 Vue3 中处理 img 标签图片加载错误的问题",
            "viewCount": "6"
        },
        {
            "createTime": "2022-03-14 00:27:57",
            "id": "1",
            "thumbnail": "https://i.niupic.com/images/2022/03/14/9Ws2.png",
            "title": "如何在 pyqt 中解决国际化 tr() 函数不管用的问题",
            "viewCount": "5"
        }
    ],
    "msg": "操作成功"
}
    return ho
from .exception.Jwt import check_token_blog
@article_api.route("/articleList", methods=["GET"])
@api.validate(
    resp=DocResponse(Success()),
    # security=[AuthorizationBearerSecurity],
    tags=["博客"],
)
@check_token_blog
def get_article_articleList():
    """
    获取文章列表
    """
    data = {
    "code": 200,
    "data": {
        "rows": [
            {
                "categoryName": "markdown",
                "createTime": "2022-01-12 21:16:07",
                "id": "4",
                "summary": "这篇博客用来测试 Kila Kila Blog 的正文样式",
                "thumbnail": "https://i.niupic.com/images/2022/03/11/9Wl7.jpg",
                "title": "测试 Kila Kila Blog 的博客样式",
                "viewCount": "72"
            },
            {
                "categoryName": "python",
                "createTime": "2022-03-14 00:27:57",
                "id": "1",
                "summary": "前言\n有些时候我们在父类中使用了 self.tr('XXX')，使用 Qt Linguist 完成翻译并导出 qm 文件后，发现子类中仍然是英文原文。比如下面这段代码：\nclass AlbumCardBase(QWidget):\n    &quot;&quot;&quot; 专辑卡基类 &quot;",
                "thumbnail": "https://i.niupic.com/images/2022/03/14/9Ws2.png",
                "title": "如何在 pyqt 中解决国际化 tr() 函数不管用的问题",
                "viewCount": "5"
            }
        ],
        "total": "6"
    },
    "msg": "操作成功"
}
    return data

@article_api.route("/<int:id>", methods=["GET"])
@api.validate(
    resp=DocResponse(Success()),
    # security=[AuthorizationBearerSecurity],
    tags=["博客"],
)
def get_article(id):
    """
    获取文章详情
    """
    data = {
    "code": 200,
    "data": {
        "categoryId": "2",
        "categoryName": "python",
        "content": "# 前言\n\n有些时候我们在父类中使用了 `self.tr('XXX')`，使用 Qt Linguist 完成翻译并导出 qm 文件后，发现子类中仍然是英文原文。比如下面这段代码：\n\n```python\nclass AlbumCardBase(QWidget):\n    \"\"\" 专辑卡基类 \"\"\"\n\n    def __init__(self, parent=None):\n        super().__init__(parent=parent)\n        self.playButton = BlurButton(\n            self,\n            (30, 65),\n            \":/images/album_tab_interface/Play.png\",\n            self.coverPath,\n            self.tr('Play')\n        )\n        self.addToButton = BlurButton(\n            self,\n            (100, 65),\n            \":/images/album_tab_interface/Add.png\",\n            self.coverPath,\n            self.tr('Add to')\n        )\n```\n\n父类 `AlbumCardBase` 中有两处使用了 `tr` 函数，分别翻译为 `播放` 和 `添加到`，但是在子类中这些文本仍然会显示为 `Play` 和 `Add to`，下面来看看如何解决这个问题。\n\n# 解决过程\n\n生成的 ts 文件中，有这样一段代码：\n\n```xml\n<context>\n    <name>AlbumCardBase</name>\n    <message>\n        <location filename=\"../../components/album_card/album_card_base.py\" line=\"50\"/>\n        <source>Add to</source>\n        <translation>添加到</translation>\n    </message>\n    <message>\n        <location filename=\"../../components/album_card/album_card_base.py\" line=\"43\"/>\n        <source>Play</source>\n        <translation>播放</translation>\n    </message>\n</context>\n```\n\n可以看到上述代码描述了源文的位置和内容以及译文，但是只对父类 `AlbumCardBase` 起作用。要想对子类应用上述规则，只需复制粘贴再修改 `<name>` 标签中的类名即可，比如 `AlbumCard` 为子类，那么只需添加下述代码：\n\n```xml\n<context>\n    <name>AlbumCard</name>\n    <message>\n        <location filename=\"../../components/album_card/album_card_base.py\" line=\"50\"/>\n        <source>Add to</source>\n        <translation>添加到</translation>\n    </message>\n    <message>\n        <location filename=\"../../components/album_card/album_card_base.py\" line=\"43\"/>\n        <source>Play</source>\n        <translation>播放</translation>\n    </message>\n</context>\n```\n\n完成上述步骤后导出 qm 文件即可。\n",
        "createTime": "2022-03-14 00:27:57",
        "id": "1",
        "summary": "前言\n有些时候我们在父类中使用了 self.tr('XXX')，使用 Qt Linguist 完成翻译并导出 qm 文件后，发现子类中仍然是英文原文。比如下面这段代码：\nclass AlbumCardBase(QWidget):\n    &quot;&quot;&quot; 专辑卡基类 &quot;",
        "tags": [
            {
                "id": "2",
                "name": "python"
            },
            {
                "id": "8",
                "name": "pyqt"
            }
        ],
        "thumbnail": "https://i.niupic.com/images/2022/03/14/9Ws2.png",
        "title": "如何在 pyqt 中解决国际化 tr() 函数不管用的问题",
        "viewCount": "5"
    },
    "msg": "操作成功"
}
    return data


@article_api.route("/previousNextArticle/<int:id>", methods=["GET"])
@api.validate(
    resp=DocResponse(Success()),
    # security=[AuthorizationBearerSecurity],
    tags=["博客"],
)
def get_article_previousNextArticle(id):
    """
    获取上一篇和下一篇文章
    """
    data = {
    "code": 200,
    "data": {
        "categoryId": "2",
        "categoryName": "python",
        "content": "# 前言\n\n有些时候我们在父类中使用了 `self.tr('XXX')`，使用 Qt Linguist 完成翻译并导出 qm 文件后，发现子类中仍然是英文原文。比如下面这段代码：\n\n```python\nclass AlbumCardBase(QWidget):\n    \"\"\" 专辑卡基类 \"\"\"\n\n    def __init__(self, parent=None):\n        super().__init__(parent=parent)\n        self.playButton = BlurButton(\n            self,\n            (30, 65),\n            \":/images/album_tab_interface/Play.png\",\n            self.coverPath,\n            self.tr('Play')\n        )\n        self.addToButton = BlurButton(\n            self,\n            (100, 65),\n            \":/images/album_tab_interface/Add.png\",\n            self.coverPath,\n            self.tr('Add to')\n        )\n```\n\n父类 `AlbumCardBase` 中有两处使用了 `tr` 函数，分别翻译为 `播放` 和 `添加到`，但是在子类中这些文本仍然会显示为 `Play` 和 `Add to`，下面来看看如何解决这个问题。\n\n# 解决过程\n\n生成的 ts 文件中，有这样一段代码：\n\n```xml\n<context>\n    <name>AlbumCardBase</name>\n    <message>\n        <location filename=\"../../components/album_card/album_card_base.py\" line=\"50\"/>\n        <source>Add to</source>\n        <translation>添加到</translation>\n    </message>\n    <message>\n        <location filename=\"../../components/album_card/album_card_base.py\" line=\"43\"/>\n        <source>Play</source>\n        <translation>播放</translation>\n    </message>\n</context>\n```\n\n可以看到上述代码描述了源文的位置和内容以及译文，但是只对父类 `AlbumCardBase` 起作用。要想对子类应用上述规则，只需复制粘贴再修改 `<name>` 标签中的类名即可，比如 `AlbumCard` 为子类，那么只需添加下述代码：\n\n```xml\n<context>\n    <name>AlbumCard</name>\n    <message>\n        <location filename=\"../../components/album_card/album_card_base.py\" line=\"50\"/>\n        <source>Add to</source>\n        <translation>添加到</translation>\n    </message>\n    <message>\n        <location filename=\"../../components/album_card/album_card_base.py\" line=\"43\"/>\n        <source>Play</source>\n        <translation>播放</translation>\n    </message>\n</context>\n```\n\n完成上述步骤后导出 qm 文件即可。\n",
        "createTime": "2022-03-14 00:27:57",
        "id": "1",
        "summary": "前言\n有些时候我们在父类中使用了 self.tr('XXX')，使用 Qt Linguist 完成翻译并导出 qm 文件后，发现子类中仍然是英文原文。比如下面这段代码：\nclass AlbumCardBase(QWidget):\n    &quot;&quot;&quot; 专辑卡基类 &quot;",
        "tags": [
            {
                "id": "2",
                "name": "python"
            },
            {
                "id": "8",
                "name": "pyqt"
            }
        ],
        "thumbnail": "https://i.niupic.com/images/2022/03/14/9Ws2.png",
        "title": "如何在 pyqt 中解决国际化 tr() 函数不管用的问题",
        "viewCount": "5"
    },
    "msg": "操作成功"
    }
    return data

@article_api.route("/updateViewCount/<id>", methods=["PUT"])
@api.validate(
    resp=DocResponse(Success()),
    # security=[AuthorizationBearerSecurity],
    tags=["博客"],
)
def get_article_updateViewCount(id):
    """
    更新阅读数量
    """
    data = {
    "code": 200,
    "msg": "操作成功"
}
    return data


