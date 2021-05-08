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