import yaml
from typing import Dict
import asyncio

class RedisConfig:
    host: str
    port: int

    def __init__(self, obj: Dict) -> None:
        self.host = obj.get('host')
        self.port = obj.get('port')

file = open('config.yaml')
result: Dict = yaml.load(file, Loader=yaml.FullLoader) 
redisConf = RedisConfig(result.get('redis'))
print(f"host - {redisConf.host} port - {redisConf.port}")

testinStrArray = ['testing', 'testing1', 'testing2', 'testing3']

joinStr = '&'.join(item for item in testinStrArray)
print(joinStr)

async def test_asyncio():
    while True:
        print('testing sleep 3 detik')
        await asyncio.sleep(3)

asyncio.ensure_future(test_asyncio())
loop = asyncio.new_event_loop()
loop.run_until_complete(test_asyncio())