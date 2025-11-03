from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from database import get_db
from vendor_profile import models
from cloudinary_setup import cloudinary
import cloudinary.uploader

router = APIRouter(prefix="/vendor", tags=["Vendor Media"])

@router.post("/upload-media")
async def upload_vendor_media(
    vendor_id: str = Form(...),
    media_type: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    allowed_types = ["logo", "banner", "item"]
    if media_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid media_type. Use 'logo', 'banner', or 'item'.")

    vendor = db.query(vendor).filter(vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    try:
        upload_result = uploader.upload(file.file, folder=f"craveseat/vendors/{vendor_id}")
        image_url = upload_result.get("secure_url")

        if not image_url:
            raise HTTPException(status_code=500, detail="Failed to upload image to Cloudinary")

        # Update vendor fields dynamically
        if media_type == "logo":
            vendor.logo_url = image_url
        elif media_type == "banner":
            vendor.banner_url = image_url
        elif media_type == "item":
            vendor.item_images = (vendor.item_images or []) + [image_url]

        db.commit()
        db.refresh(vendor)

        return {"message": f"{media_type.capitalize()} uploaded successfully", "image_url": image_url, "vendor": vendor}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
