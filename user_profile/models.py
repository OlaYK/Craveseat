from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from authentication.database import Base
from authentication.models import User

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    bio = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    delivery_address = Column(String, nullable=True)
    image_url = Column(String, nullable=True)  # Cloudinary URL

    user = relationship("User", back_populates="profile")