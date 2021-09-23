import asyncio
import aiohttp
from datetime import datetime
import time
import pandas as pd

SNAPSHOT_REST_URL = "https://api.binance.com/api/v1/depth"
# n = 0
# while n < 10:
#     n+=1
#     print(f"n - {n} time - {datetime.now()}")
#     time.sleep(10)

async def get_snapshot():
    params: Dict = {"limit": 100, "symbol": "btc_idr"} if limit != 0 \
            else {"symbol": convert_to_exchange_trading_pair(trading_pair)}
    async with aiohttp.ClientSession() as session:
        async with session.get(SNAPSHOT_REST_URL, params={"limit": 100, "symbol": "btc_idr"}) as response:
            result: aiohttp.ClientResponse = response
            print(result)


this_hour: pd.Timestamp = pd.Timestamp.utcnow().replace(minute=0, second=0, microsecond=0)
print(this_hour)
next_hour: pd.Timestamp = this_hour + pd.Timedelta(hours=1)
print(next_hour)
print(time.time())
delta: float = next_hour.timestamp() - time.time()
print(delta)