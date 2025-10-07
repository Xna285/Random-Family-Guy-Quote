from mainFunctions import *

import random

from typing import Union

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return ReturnHTML(GetQuote(random.randint(1,100)))
    

