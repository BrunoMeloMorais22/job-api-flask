import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:passport@localhost:5433/job_api"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "yasmin"