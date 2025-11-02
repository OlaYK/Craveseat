from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base, engine 
from authentication.models import User

class UserProfile(Base):
    __tablename__ = "user_profiles"

    user_id = Column(String, ForeignKey("users.id"), primary_key= True, nullable=False)
    bio = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    delivery_address = Column(String, nullable=True)
    image_url = Column(String, nullable=True) 
    updated_at = Column(DateTime(timezone=True),server_default=func.now(), onupdate=func.now(), nullable=False)    

    user = relationship("User", back_populates="profile")

