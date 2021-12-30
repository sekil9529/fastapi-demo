from fastapi import FastAPI

from app.factory import create_app


app: FastAPI = create_app()
