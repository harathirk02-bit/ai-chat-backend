# AI Career Operating System Backend

## Project Description

AI Career Operating System is an intelligent web application that helps students analyze resumes, assess skills, generate career roadmaps, and receive AI-powered career guidance.

---

## Features

- User Registration and Login
- JWT Authentication
- Resume Upload
- Resume Analysis
- Skill Assessment Test
- Career Recommendation
- Roadmap Generator
- AI Chatbot
- Protected APIs
- Swagger Authorization

---

## Technologies Used

- FastAPI
- Python
- SQLite
- SQLAlchemy
- JWT Authentication
- Gemini API
- Machine Learning

---

## Project Structure

backend/
│
├── main.py
├── database.py
├── models.py
├── auth.py
├── requirements.txt
├── .gitignore
├── README.md
├── .env
│
├── uploads/
├── static/
│
├── routes/
├── utils/
├── schemas/
└── services/

---

## Installation

Install required packages:

pip install -r requirements.txt

---

## Run Project

uvicorn main:app --reload

---

## Swagger Documentation

http://127.0.0.1:8000/docs

---

## Authentication Flow

1. Register User
2. Login User
3. Get JWT Token
4. Click Authorize
5. Paste Token
6. Access Protected APIs

---

## Developed By

Team AI Career OS