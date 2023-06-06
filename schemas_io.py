from pydantic import BaseModel,Field
from typing import Optional



class HeartbeatResponse(BaseModel):
    status:str = "alive"

# ceci est la collection pour la base de donnés mongo db 
class UserModel(BaseModel):
    full_name:str = Field(None,description="Full name of the user")
    role:str = Field(None,description="Role of the user")
    email:str = Field(None,description="Email of the user")
    password:str = Field(None,description="Password of the user")
    phone_number:str =  Field(None,description="Phone number of the user")
    is_active:bool = Field(None,description="Is user active")
    is_verified:bool = Field(None,description="Is user verified")
    date_registered: Optional[str] = Field(None)
    last_login: Optional[str] = Field(None)

class CreateUseModel(BaseModel):
    full_name:str = Field(None,description="Full name of the user")
    role:str = Field(None,description="Role of the user")
    email:str = Field(None,description="Email of the user")
    password:str =  Field(None,description="Password of the user")
    phone_number:str =  Field(None,description="Phone number of the user")
    is_active:bool = Field(None,description="Is user active")
    is_verified:bool = Field(None,description  ="Is user verified")
    date_registered: Optional[str] = Field(None)
    last_login: Optional[str] = Field(None)

class UpdateUserModel(BaseModel):
    full_name:Optional[str] = Field(None,description="Full name  of the user")
    role:Optional[str] = Field(None,description="Role of the user")
    email:Optional[str] = Field(None,description="Email of the user")
    password:Optional[str] = Field(None,description="Password of the user")
    phone_number:Optional[str] = Field(None,description="Phone number of the user")
    is_active:Optional[bool] = Field(None,description="Is user active")
    is_verified:Optional[bool] = Field(None,description="Is  user verified")
    date_registered: Optional[str] = Field(None)
    last_login: Optional[str] = Field(None)

class DeleteUserModel(BaseModel):
    email:str = Field(None,description="Email of the user")

class UserLoginModel(BaseModel):
    email:str = Field(None,description="Email of the user")
    password:str = Field(None,description="Password of the user")

class UserLoginResponse(BaseModel):
    access_token:str = Field(None,description="Access token of the user")
    token_type:str = Field(None,description="Token type of the user") 



