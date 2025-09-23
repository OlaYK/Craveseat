from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from database import Base
import shortuuid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=shortuuid.uuid, unique=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)




