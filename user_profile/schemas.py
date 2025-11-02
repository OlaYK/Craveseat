from pydantic import BaseModel
from typing import Optional


class UserProfileBase(BaseModel):
    bio: Optional[str] = None
    phone_number: Optional[str] = None
    delivery_address: Optional[str] = None
    


class UserProfileCreate(UserProfileBase):
  pass 

class UserProfileUpdate(UserProfileBase):
    pass


class UserProfile(UserProfileBase):
    user_id:str
    image_url: Optional[str] = None

    class Config:
        from_attributes = True 


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str

class UserProfileUpdate(BaseModel):
    bio: Optional[str] = None
    phone_number: Optional[str] = None
    delivery_address: Optional[str] = None
    image_url: Optional[str] = None  