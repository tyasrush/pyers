from fastapi import FastAPI
from ddtrace import tracer
tracer.configure(
    hostname="localhost",
    port="8126",
)
app = FastAPI()

@app.get("/test")
def testing_endpoint():
    return {"name": "test" }

