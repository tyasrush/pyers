# from fastapi import FastAPI
# from ddtrace import tracer
# tracer.configure(
#     hostname="localhost",
#     port="8126",
# )
# app = FastAPI()

# @app.get("/test")
# def testing_endpoint():
#     return {"name": "test" }

test1 = [1,2,3,4]
print(test1 for i in test1)

def halo_test():
    try:
        results = 'testing results'
    except Exception as e:
        print(e)
    
    return results

print(halo_test())


def test_switch(test_param: str) -> str:
    switch_cases = { "test": "Benar", "test1": "Benar" }
    if switch_cases.get(test_param) == None:
        return 'Tidak benar'

    return switch_cases.get(test_param)

print(test_switch("test3"))

def testing_number():
    return 2**5

print(f'testing number with double asterisk {testing_number()}')

class TestingErrorCustom(Exception):
    def __init__(self, message, code):
        super(TestingErrorCustom, self).__init__(message, code)
        self.msg = message
        self.code = code

class NotFound(TestingErrorCustom):
    def __init__(self) -> None:
        message = 'testing aja'
        code = 400
        super().__init__(message, code)

def test_error():
    try:
        raise NotFound()
    except Exception as err:
        if err.code != None and err.code == NotFound().code:
            print(err)

        raise err

# test_error()

test_num = 9
if test_num != 0:
    print('number valid')

from time import time
from datetime import datetime

num_e = int(time() * 1e3)
print(str(num_e))
to_date = datetime.fromtimestamp(int(time()))
print(to_date)