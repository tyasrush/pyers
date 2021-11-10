# import asyncio

# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({number}), currently i={i}...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")
#     return f

# async def main():
#     # Schedule three calls *concurrently*:
#     L = await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#     print(L)

# asyncio.run(main())


import socket
host = socket.gethostbyname(socket.gethostname())

print(host)

try:
    test_if = "test2"
    if test_if == "test":
        order = "test"
    if test_if == "test1":
        order = "test1"

    raise Exception("test")
except Exception:
    print(order)
