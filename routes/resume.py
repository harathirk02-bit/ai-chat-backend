from fastapi import APIRouter, UploadFile, File, Depends
from utils.jwt_handler import security

from services.resume_service import analyze_resume

import os

router = APIRouter()


@router.post("/upload-resume")

async def upload_resume(

    file: UploadFile = File(...),

    credentials=Depends(security)

):

    upload_folder = "uploads"

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    filepath = os.path.join(

        upload_folder,

        file.filename

    )

    with open(

        filepath,

        "wb"

    ) as f:

        content = await file.read()

        f.write(content)

    result = analyze_resume(
        filepath
    )

    return result