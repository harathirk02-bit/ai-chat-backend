from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return token