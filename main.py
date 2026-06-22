from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base

from routes.user import router as user_router
from routes.resume import router as resume_router
from routes.test import router as test_router
from routes.roadmap import router as roadmap_router
from routes.chatbot import router as chatbot_router

from utils.helpers import create_upload_folder


# Create Database Tables
Base.metadata.create_all(bind=engine)

# Create Upload Folder Automatically
create_upload_folder()

# FastAPI App
app = FastAPI(

    title="AI Career Operating System",

    description="""
    AI-powered career guidance platform
    with JWT authentication, resume analysis,
    roadmap generation, and AI chatbot.
    """,

    version="1.0.0"
)

# ADD THIS PART

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home API
@app.get("/")
def home():

    return {
        "message": "AI Career OS Backend Running Successfully"
    }


# Include Routes
app.include_router(user_router)

app.include_router(resume_router)

app.include_router(test_router)

app.include_router(roadmap_router)

app.include_router(chatbot_router)