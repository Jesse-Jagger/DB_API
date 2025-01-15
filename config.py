import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    # Loads environment variables from .env file
    MONGO_URI = os.getenv("MONGO_URI")
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.getenv("REDIS_URL")