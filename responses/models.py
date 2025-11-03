from sqlalchemy import Column, String, Text, ForeignKey, DateTime, Enum as SAEnum, func
from sqlalchemy.orm import relationship
from database import Base
import shortuuid
from enum import Enum as PyEnum


class ResponseStatus(PyEnum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    completed = "completed"


class Response(Base):
    __tablename__ = "responses"

    id = Column(String, primary_key=True, default=shortuuid.uuid, index=True)
    craving_id = Column(String, ForeignKey("cravings.id"), nullable=False, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    
    message = Column(Text, nullable=False)
    status = Column(SAEnum(ResponseStatus), default=ResponseStatus.pending, nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    craving = relationship("Craving", back_populates="responses")
    user = relationship("User", back_populates="responses")