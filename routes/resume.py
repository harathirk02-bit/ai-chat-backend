from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from utils.jwt_handler import security
from utils.helpers import allowed_file
from services.resume_service import analyze_resume

router = APIRouter()


# Upload Resume API
@router.post("/upload-resume")
def upload_resume(
    file: UploadFile = File(...),
    credentials = Depends(security)
):

    if not allowed_file(file.filename):

        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files allowed"
        )

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:

        f.write(file.file.read())

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename
    }


# Resume Analysis API
@router.get("/resume-analysis")
def resume_analysis(
    credentials = Depends(security)
):

    result = analyze_resume()

    return result