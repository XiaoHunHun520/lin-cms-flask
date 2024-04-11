"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from lin import InfoCrud as Base
from sqlalchemy import Column, Integer, String, Text

class BlogArticle(Base):
    # 文章
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 标题
    title = Column(String(256))
    # 文章内容
    content = Column(Text)
    # 文章摘要
    summary = Column(String(1024))
    # 所属分类id
    category_id = Column(Integer)
    # 缩略图
    thumbnail = Column(String(256))
    # 是否置顶（0否，1是）
    is_top = Column(Integer)
    # 状态（0已发布，1草稿）
    status  = Column(Integer)
    # 访问量
    view_count  = Column(Integer)
    # 是否允许评论 1是，0否
    is_comment  = Column(Integer)


class BlogArticletag(Base):
    # 文章-标签表
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 文章 ID
    article_id = Column(Integer)
    # 标签 ID
    tag_id = Column(Integer)

class BlogCategory(Base):
    # 分类表
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 分类名
    name = Column(String(128))
    # 父分类id，如果没有父分类为-1
    pid = Column(String(32))
    # 描述
    description = Column(String(512))
    # 状态0:正常,1禁用
    status = Column(Integer)


class BlogComment(Base):
    # 评论表
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 文章id
    article_id = Column(Integer)
    # 评论内容
    content = Column(String(512))

