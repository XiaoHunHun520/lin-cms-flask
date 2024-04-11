from typing import List, Optional
from pydantic import Field, validator
from lin import BaseModel,ParameterError
import re

class BookQuerySearchSchema(BaseModel):
    q: Optional[str] = str()

class DyInSchema(BaseModel):
    url: str = Field(description="用户名")
    @validator("url")
    def check_url(cls, v, values, **kwargs):
        paa = re.compile('https://v.douyin.com/(.*?)/')
        # 匹配输入内容是否带抖音链接
        urls = re.findall(paa, v)
        if not urls:
            raise ParameterError("请输入正确的抖音视频分享链接")
        return v