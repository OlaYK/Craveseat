from fastapi import FastAPI
from authentication import auth as auth_routes
from user_profile import routes as profile_routes

app = FastAPI(title = "CraveSeat App")

app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(profile_routes.router, prefix="/profile", tags=["User Profile"])
