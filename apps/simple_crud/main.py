import logging
from fastapi import FastAPI, Request, Response
import uuid
import time
import sys
from typing import Tuple

app = FastAPI()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_format = logging.StreamHandler(sys.stdout)
log_format.setFormatter(logging.Formatter('%(asctime)s:%(name)s - %(levelname)s -> %(funcName)s:%(lineno)d - %(message)s'))

logger.addHandler(log_format)
logger.info("testing debug")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = str(uuid.uuid4())
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    
    # Adding tuple request id to track log
    id_header: Tuple[bytes] = ("x-request-id".encode(), idem.encode())
    request.headers.__dict__["_list"].append(id_header)
    # print(request.headers)
    response: Response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    response.headers["X-Req-ID"] = idem
    
    return response


@app.get("/")
async def root(req: Request):
    logger.info(req.headers['x-request-id'])
    return {"status": "alive"}