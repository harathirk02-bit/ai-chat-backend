from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException
from jose import jwt, JWTError

security = HTTPBearer()

SECRET_KEY = "secret123"
ALGORITHM = "HS256"


def get_current_user(
    credentials=Depends(security)
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )