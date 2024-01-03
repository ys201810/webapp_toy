# coding=utf-8
import pathlib
import logging
import pandas as pd
from fastapi import FastAPI
from post_classes import Person

app = FastAPI()

backend_base_path = pathlib.Path().cwd().parent
log_file = backend_base_path / 'log' / 'backend.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@app.get("/")
async def read_root():
    logger.info('root access.')
    return {'hello': 'world'}

@app.get("/get_all")
async def get_all_info():
    logger.info('get all info access.')
    df = pd.read_csv(backend_base_path / 'data' / 'data.csv')
    return df.to_dict(orient='records')


@app.post("/save_person")
async def save_person(person_info: Person):
    df = pd.read_csv(backend_base_path / 'data' / 'data.csv')
    df = pd.concat([df, pd.DataFrame({
        'name': person_info.name,
        'age': person_info.age
    }, index=[0]), ], ignore_index=True)
    df.to_csv(backend_base_path / 'data' / 'data.csv', index=False)
    logger.info('post save info access.')
    return f'save success name:{person_info.name} age:{person_info.age}'
