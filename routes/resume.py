from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from utils.jwt_handler import get_current_user
from utils.helpers import allowed_file
from services.resume_service import analyze_resume

import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# Upload Resume API
@router.post("/upload-resume")
def upload_resume(
    file: UploadFile = File(...),
    user=Depends(get_current_user)
):

    if not allowed_file(file.filename):

        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files allowed"
        )

    file_location = f"{UPLOAD_DIR}/{file.filename}"

    try:

        with open(file_location, "wb") as f:

            f.write(file.file.read())

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="File upload failed"
        )

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename
    }


# Resume Analysis API
@router.get("/resume-analysis")
def resume_analysis(
    user=Depends(get_current_user)
):

    result = analyze_resume()

    return result