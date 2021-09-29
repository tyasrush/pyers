import aioredis
import asyncio
import json

async def main():
    redis = aioredis.from_url("redis://localhost:6379")
    async with redis.client() as cl:
        await cl.hset("btcusdt", "bids", """[{ "Price": "42442.00000000", "Qty": "0.09765000"},{"Price": "42439.88000000", "Qty": "0.07450000"},{ "Price": "42438.90000000","Qty": "0.20000000"}]""")
        result = await cl.hget('btcusdt', 'bids')
        json_results = json.loads(result)
        for item in json_results:
            print(item.get('Price'))
            print(item.get('Qty'))

async def get_value():
    result = await redis.hget("btcusdt", "bids")
    print(f"result - {result}")

asyncio.run(main())