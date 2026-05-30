from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User

from auth import (
    hash_password,
    verify_password,
    create_access_token
)

from schemas.user_schema import (
    UserRegister,
    UserLogin
)

from utils.jwt_handler import get_current_user

router = APIRouter()


# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------
# REGISTER API
# -------------------------
@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)

    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return {
        "message": "Registration Successful"
    }


# -------------------------
# LOGIN API
# -------------------------
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    token = create_access_token(
        data={"sub": existing_user.email, "user_id": existing_user.id}
    )

    return {
        "message": "Login Successful",
        "access_token": token,
        "token_type": "bearer"
    }


# -------------------------
# PROFILE API (PROTECTED)
# -------------------------
@router.get("/profile")
def profile(user=Depends(get_current_user)):

    return {
        "message": "Authorized User Profile",
        "user": user
    }