from flask import Blueprint

# from app.api.blog.user import user_api


def create_blog():
    blog = Blueprint("blog", __name__)
    from app.api.blog.user import user_api
    from app.api.blog.article import article_api
    from app.api.blog.archive import archive_api

    blog.register_blueprint(user_api, url_prefix="/user")
    blog.register_blueprint(article_api, url_prefix="/article")
    blog.register_blueprint(archive_api, url_prefix="/archive")
    return blog
