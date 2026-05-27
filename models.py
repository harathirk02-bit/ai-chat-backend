from sqlalchemy import Column, Integer, String, Text
from database import Base, engine


# Users Table
class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    email = Column(String(150), unique=True)

    password = Column(String(255))


# Resume Table
class Resume(Base):

    __tablename__ = "resumes"

    resume_id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer)

    file_name = Column(String(255))

    extracted_skills = Column(Text)

    resume_score = Column(Integer)


# Create Tables
Base.metadata.create_all(bind=engine)

print("Database Tables Created Successfully")
