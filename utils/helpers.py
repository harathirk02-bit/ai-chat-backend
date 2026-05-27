import os


def create_upload_folder():

    if not os.path.exists("uploads"):
        os.makedirs("uploads")


def allowed_file(filename):

    allowed_extensions = [
        ".pdf",
        ".docx"
    ]

    return filename.endswith(
        tuple(allowed_extensions)
    )