from lin import BaseModel, ParameterError
from pydantic import Field, validator



class LoginSchema(BaseModel):
    userName: str = Field(description="用户名")
    password: str = Field(description="密码")

class RegisterSchema(BaseModel):
    userName: str = Field(description="用户名")
    password: str = Field(description="密码")
    email: str = Field(description="邮箱")
    nickName: str = Field(description="昵称")


class LoginTokenSchema(BaseModel):
    access_token: str = Field(description="access_token")
    refresh_token: str = Field(description="refresh_token")