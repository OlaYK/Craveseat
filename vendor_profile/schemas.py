# vendor_profile/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from enum import Enum


# ---------------- ENUMS ----------------
class VendorStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    suspended = "suspended"


class VerificationStatus(str, Enum):
    pending = "pending"
    verified = "verified"
    rejected = "rejected"


class AvailabilityStatus(str, Enum):
    available = "available"
    out_of_stock = "out_of_stock"


# ---------------- SERVICE CATEGORY ----------------
class ServiceCategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class ServiceCategoryResponse(ServiceCategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# ---------------- VENDOR ITEM ----------------
class VendorItemBase(BaseModel):
    item_name: str
    item_description: Optional[str] = None
    item_price: Decimal
    item_image_url: Optional[str] = None
    availability_status: Optional[AvailabilityStatus] = AvailabilityStatus.available


class VendorItemCreate(VendorItemBase):
    pass


class VendorItemResponse(VendorItemBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# ---------------- VENDOR PROFILE ----------------
class VendorProfileBase(BaseModel):
    business_name: Optional[str] = None
    service_category_id: Optional[int] = None
    vendor_address: Optional[str] = None
    vendor_phone: Optional[str] = None
    vendor_email: Optional[EmailStr] = None
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None


class VendorProfileCreate(VendorProfileBase):
    pass


class VendorProfileUpdate(VendorProfileBase):
    status: Optional[VendorStatus] = None
    verification_status: Optional[VerificationStatus] = None


class VendorProfileResponse(VendorProfileBase):
    vendor_id: str
    rating: Optional[Decimal] = None
    is_verified: bool
    status: VendorStatus
    verification_status: VerificationStatus
    created_at: datetime
    updated_at: datetime
    category: Optional[ServiceCategoryResponse]
    items: List[VendorItemResponse] = []

    class Config:
        orm_mode = True