import os
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"  # Upewnij się, że pasuje do istniejącej tabeli

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    gender = Column(String)
    health_goal = Column(String)
    exercise_frequency = Column(String)
    meal_prep_time = Column(String)
    #number_of_days = Column(Integer)
    weekly_budget = Column(Float)
    disliked_foods = Column(String)

class Allergies(Base):
    __tablename__ = "allergies"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String)


class User_Allergies(Base):
    __tablename__ = "user_allergies"
    user_id = Column(Integer, ForeignKey("users.id"),primary_key=True)
    allergy_id = Column(Integer, ForeignKey("allergies.id"),primary_key=True)


