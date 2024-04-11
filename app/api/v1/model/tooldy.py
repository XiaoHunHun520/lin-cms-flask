"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from lin import InfoCrud as Base
from sqlalchemy import Column, Integer, String


class ToolDy(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer)
    author = Column(String(30))
    share_title = Column(String(128))
    video_url = Column(String(256))