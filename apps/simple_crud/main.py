import logging
from fastapi import FastAPI, Request, Response
import uuid
import time
import sys
from typing import Tuple
import json

from starlette.responses import JSONResponse

app = FastAPI()

cust_log = logging.getLogger()
cust_log.setLevel(logging.INFO)
log_format = logging.StreamHandler(sys.stdout)
log_format.setFormatter(logging.Formatter('%(asctime)s:%(name)s - %(levelname)s -> %(funcName)s:%(lineno)d - %(message)s'))

cust_log.addHandler(log_format)
class AsyncIteratorWrapper:
    def __init__(self, obj):
        self._it = iter(obj)
    def __aiter__(self):
        return self
    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = str(uuid.uuid4())
    start_time = time.time()
    
    # Adding tuple request id to track log
    id_header: Tuple[bytes] = ("x-request-id".encode(), idem.encode())
    request.headers.__dict__["_list"].append(id_header)
    response: Response = await call_next(request)

    req_param = {}
    req_body = await request.body()
    if len(req_body.decode()) > 0:
        req_param = await request.json()

    # Consuming FastAPI response and grabbing body here
    resp_body = [section async for section in response.__dict__['body_iterator']]
    # Repairing FastAPI response
    response.__setattr__('body_iterator', AsyncIteratorWrapper(resp_body))

    # Formatting response body for logging
    rb = json.loads(resp_body[0].decode())
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    cust_log.info(f"rid={idem} duration={formatted_process_time}ms request={req_param} response={rb} status_code={response.status_code} path={request.url.path}")
    response.headers["X-Req-ID"] = idem
    response.headers["X-Duration"] = f"{formatted_process_time}ms"
    
    return response


@app.get("/")
async def root(req: Request):
    return JSONResponse(content={"status": "alive"})

    