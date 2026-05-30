from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

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

from utils.jwt_handler import security

router = APIRouter()


# Database Connection
def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


# Register API
@router.post("/register")
def register(

    user: UserRegister,

    db: Session = Depends(get_db)

):

    existing_user = db.query(
        User
    ).filter(

        User.email == user.email

    ).first()

    if existing_user:

        raise HTTPException(

            status_code=400,

            detail="Email already exists"

        )

    hashed_password = hash_password(
        user.password
    )

    new_user = User(

        name=user.name,

        email=user.email,

        password=hashed_password

    )

    db.add(
        new_user
    )

    db.commit()

    return {

        "message":
        "Registration Successful"

    }


# Login API
@router.post("/login")
def login(

    user: UserLogin,

    db: Session = Depends(get_db)

):

    existing_user = db.query(
        User
    ).filter(

        User.email == user.email

    ).first()

    if not existing_user:

        raise HTTPException(

            status_code=404,

            detail="User Not Found"

        )

    password_check = verify_password(

        user.password,

        existing_user.password

    )

    if not password_check:

        raise HTTPException(

            status_code=401,

            detail="Incorrect Password"

        )

    token = create_access_token(

        data={

            "sub":
            existing_user.email

        }

    )

    return {

        "message":
        "Login Successful",

        "access_token":
        token,

        "token_type":
        "bearer"

    }


# Protected Profile API
@router.get("/profile")
def profile(

    credentials = Depends(security)

):

    return {

        "message":
        "Authorized User Profile"

    }