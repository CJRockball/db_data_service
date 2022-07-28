from fastapi import FastAPI
from app.main import tips


app = FastAPI()

app.include_router(tips, prefix='/tips', tags=['tips'])