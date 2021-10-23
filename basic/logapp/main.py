import logging
import os
import sys
import time
from decimal import Decimal
import pandas as pd

logger = logging.getLogger()
logger.setLevel(logging.INFO)

lH = logging.StreamHandler(sys.stdout)
# lH.setLevel(logging.INFO)
lH.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'))

# lE = logging.StreamHandler(sys.stderr)
# lE.setLevel(logging.ERROR)
# lE.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'))

logger.addHandler(lH)
# logger.addHandler(lE)

# while True:
#     logger.info("testing info masuk mana nih")
#     logger.error("testing error masuk mana nih")
#     logger.debug("testing debug masuk mana nih")
#     this_hour: pd.Timestamp = pd.Timestamp.utcnow().replace(minute=0, second=0, microsecond=0)
#     next_hour: pd.Timestamp = this_hour + pd.Timedelta(hours=1)
#     delta: float = next_hour.timestamp() - time.time()
#     print(f"delta - {delta}")
#     time.sleep(3.0)

test_bagi = Decimal(10)// Decimal(2)
print(test_bagi)

import asyncio
from async_timeout import timeout
from functools import partial

def testing_return(stt: str):
    return stt + ': testingaijoifajds'

async def single_run_sync_with_async(func):
    try:
        coro = loop.run_in_executor(None, func)

        # create future to get result and execute
        ftr: asyncio.Future = loop.create_future()

        # put set result for future 
        _= asyncio.ensure_future(get_value(ftr, coro))
        return await ftr
    except Exception as e:
        logging.info(f"error binance get account - {e}")


async def get_value(future: asyncio.Future, coro):
    future.set_result(await coro)

# test = testing_return("halo")

loop = asyncio.new_event_loop()
result = loop.run_until_complete(single_run_sync_with_async(partial(testing_return, 'testing')))

print(f"results - {result}")