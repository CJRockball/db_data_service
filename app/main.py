from fastapi import FastAPI, Request, APIRouter, HTTPException, Form
import pathlib
from starlette.responses import FileResponse
import pandas as pd
import json
import logging
from typing import Optional, List
from pydantic import BaseModel
#from app.utils import get_logger
from app.db_utils import get_db_data

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
LOG_DIR = ROOT_DIR / 'logs'
favicon_path = ROOT_DIR / "data/favicon.png"

#LOG = get_logger('tips_dataset')

tips = APIRouter()


@tips.get("/favicon.ico", include_in_schema=False)
async def favicon():
    #logging.info("Opened favicon")
    return FileResponse(favicon_path)


@tips.get("/")
async def index_get():
    #logging.info("Opened index page")
    return {'message':'hello world tips'}


@tips.get("/test_data")
async def weight_data_page():
    #logging.info("Opened weight page")
    result = get_db_data("test")
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Test data not found")
    
    dfjson = result.to_json(orient="records")
    parsed = json.loads(dfjson)
    
    return parsed


@tips.get("/train_data")
async def weight_data_page():
    #logging.info("Opened weight page")
    result = get_db_data("train")
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Test data not found")
    
    dfjson = result.to_json(orient="records")
    parsed = json.loads(dfjson)
    
    return parsed