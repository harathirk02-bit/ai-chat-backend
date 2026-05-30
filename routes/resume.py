from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from utils.jwt_handler import verify_token
from utils.helpers import allowed_file

router = APIRouter()


@router.post("/upload-resume")
def upload_resume(

    file: UploadFile = File(...),

    token: str = Depends(verify_token)

):

    if not allowed_file(file.filename):

        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX Allowed"
        )

    file_location = f"uploads/{file.filename}"

    with open(
        file_location,
        "wb"
    ) as f:

        f.write(
            file.file.read()
        )

    return {

        "message":
        "Resume Uploaded Successfully",

        "filename":
        file.filename

    }