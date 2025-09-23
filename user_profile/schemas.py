
from pydantic import BaseModel
from typing import Optional


class UserProfileBase(BaseModel):
    bio: Optional[str] = None
    phone_number: Optional[str] = None
    delivery_address: Optional[str] = None
    profile_image: Optional[str] = None  


class UserProfileCreate(UserProfileBase):
    pass


class UserProfileUpdate(UserProfileBase):
    pass


class UserProfile(UserProfileBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True 


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str