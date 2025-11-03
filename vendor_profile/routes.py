from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from authentication.auth import get_current_active_user
from authentication import models as auth_models
from authentication.models import UserType
from database import get_db
from vendor_profile import crud, schemas
from cloudinary_setup import upload_image

router = APIRouter()


# ---------------- SERVICE CATEGORIES ----------------
@router.get("/categories", response_model=list[schemas.ServiceCategoryResponse])
def list_service_categories(db: Session = Depends(get_db)):
    return crud.get_service_categories(db)


# ---------------- VENDOR PROFILE ----------------
@router.post("/", response_model=schemas.VendorProfileResponse)
def create_vendor_profile(
    profile: schemas.VendorProfileCreate,
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_user),
):
    if current_user.user_type != UserType.vendor:
        raise HTTPException(status_code=403, detail="Only vendors can create a vendor profile.")

    existing_profile = crud.get_vendor_profile(db, current_user.id)
    if existing_profile:
        raise HTTPException(status_code=400, detail="Vendor profile already exists.")

    return crud.create_vendor_profile(db, current_user.id, profile)


@router.get("/", response_model=schemas.VendorProfileResponse)
def get_vendor_profile(
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_user),
):
    if current_user.user_type != UserType.vendor:
        raise HTTPException(status_code=403, detail="Only vendors can access this route.")

    profile = crud.get_vendor_profile(db, current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail="Vendor profile not found.")
    return profile


@router.put("/", response_model=schemas.VendorProfileResponse)
def update_vendor_profile(
    profile_update: schemas.VendorProfileUpdate,
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_user),
):
    if current_user.user_type != UserType.vendor:
        raise HTTPException(status_code=403, detail="Only vendors can update their profile.")

    updated_profile = crud.update_vendor_profile(db, current_user.id, profile_update)
    if not updated_profile:
        raise HTTPException(status_code=404, detail="Vendor profile not found.")
    return updated_profile


# ---------------- VENDOR ITEMS ----------------
@router.post("/items", response_model=schemas.VendorItemResponse)
def add_item(
    item: schemas.VendorItemCreate,
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_user),
):
    if current_user.user_type != UserType.vendor:
        raise HTTPException(status_code=403, detail="Only vendors can add items.")
    return crud.add_vendor_item(db, current_user.id, item)


@router.get("/items", response_model=list[schemas.VendorItemResponse])
def list_vendor_items(
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_user),
):
    if current_user.user_type != UserType.vendor:
        raise HTTPException(status_code=403, detail="Only vendors can view their items.")
    return crud.get_vendor_items(db, current_user.id)


@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendor_item(
    item_id: str,
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_user),
):
    if current_user.user_type != UserType.vendor:
        raise HTTPException(status_code=403, detail="Only vendors can delete their items.")
    
    success = crud.delete_vendor_item(db, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found.")
    return None