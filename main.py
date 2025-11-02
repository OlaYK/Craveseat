from fastapi import FastAPI
from authentication import auth as auth_routes
from user_profile import routes as profile_routes
from vendor_profile import routes as vendor_routes
from database import engine, Base, SessionLocal, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title = "CraveSeat App")

app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(profile_routes.router, prefix="/profile", tags=["User Profile"])
app.include_router(vendor_routes.router, prefix="/vendor", tags=["Vendor Profile"])

