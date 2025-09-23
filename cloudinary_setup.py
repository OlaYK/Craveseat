import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

       
cloudinary.config( 
    cloud_name = "dqwkcdb8l", 
    api_key = "619931572143789", 
    api_secret = "XeNO2iZkSc-EjTWpcaguqr3T0cM", 
    secure=True
)

def upload_image(image_file, folder="profile_images"):
    upload_result = cloudinary.uploader.upload(image_file, folder=folder)
    return upload_result.get("secure_url")
