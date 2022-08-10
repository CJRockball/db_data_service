from fastapi import FastAPI, Request, APIRouter, HTTPException, Form
import pathlib
from starlette.responses import FileResponse
import pandas as pd
import json
import logging
from typing import Optional, List
from pydantic import BaseModel
from api.db_utils import get_db_data, get_random_test_data
from typing import List

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
LOG_DIR = ROOT_DIR / 'logs'
LOG_FILE = ROOT_DIR / 'logs/test.log'
favicon_path = ROOT_DIR / "data/favicon.png"

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
)

tips = APIRouter()


class TipsData(BaseModel):
    total_bill : float
    tip : float
    sex : str
    smoker : str
    day : str
    time : str
    g_size : int

@tips.get("/favicon.ico", include_in_schema=False)
async def favicon():
    #logging.info("Opened favicon")
    return FileResponse(favicon_path)


@tips.get("/")
async def index_get():
    logging.info("Opened index page")
    return {'message':'hello world tips'}


@tips.get("/test_data", response_model=List[TipsData])
async def weight_data_page():
    logging.info("Get all test data")
    result = get_db_data("test")
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Test data not found")
    
    dfjson = result.to_json(orient="records")
    parsed = json.loads(dfjson)
    
    return parsed


@tips.get("/train_data", response_model=List[TipsData])
async def weight_data_page():
    logging.info("Get all training data")
    result = get_db_data("train")
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Test data not found")
    
    dfjson = result.to_json(orient="records")
    parsed = json.loads(dfjson)
    
    return parsed


@tips.get('/get_random_test_data', response_model=List[TipsData])
def random_test_data():
    logging.info("Return random test row")
    result = get_random_test_data()

    dfjson = result.to_json(orient="records")
    parsed = json.loads(dfjson)
    
    return parsed
    
