from typing import List
import time
import hashlib
import hmac
import asyncio
import aiohttp
from typing import (
    Any,
    Dict
)
from urllib.parse import urlencode

# def check_number():
#     for n in numbs:

params = {}

params.update({
    'method': 'getInfo',
    'timestamp': time.time() * 1000,
    'nonce': 1000
})

print(params)

signature = hmac.new(''.encode("utf8"), urlencode(params).encode("utf8"), hashlib.sha512)
        
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Key": "",
    "Sign": signature.hexdigest()
}

timee = str(time.time() * float("1e3"))
print(timee)
print(float("1e3") == 1000)

print(f"signature - {signature.hexdigest()} current time - {timee}")

class TestHTTP:
    async def main(self):
        async with aiohttp.ClientSession as session:
            async with session.post(url="https://btcapi.net/tapi", headers=headers, data=params) as response:
                print(response.status)

th = TestHTTP()


loop = asyncio.get_event_loop()
loop.run_until_complete(th.main())