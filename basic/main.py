# from pydantic import BaseModel
# from datetime import datetime
# from collections import namedtuple
# import psycopg2
# import os
# class EntityTest(BaseModel):
#     name: str

# test = EntityTest(name="test1")
# test1 = EntityTest(name="test1")
# print(test.__class__.__name__)

# print("testing name {}".format(__name__))

# print(test == test1)

# import data_type.str_class as strc

# strc.print_str()

# from data_type.str_class import Metadata

# halo = Metadata(_id='74c0a004-1ab2-53f0-8509-362d919ba2e2', account_email='jhonDoe@mail.com', table_name='GetInfo', symbol='NA', last_sync_timestamp=1578638764000, last_record_timestamp=1578638962, last_record_id='NA')
# # print(halo.__fields__)
# # print(halo.created_at)

# testingArry = [1,2,3]
# copyTest = []

# for item in testingArry:
#     copyTest.append(item)

# print(copyTest)

# # testDbParam = dict(host='localhost', port=5432, user='postgres', password='postgres', dbname='indodax_agent')
# # print(**testDbParam)
# # conn = psycopg2.connect(dsn="host='localhost' port=5432 user='postgres' password='postgres' dbname='indodax_agent'")

# # cur = conn.cursor()

# # cur.execute('SELECT _id, account_email, table_name, symbol, last_sync_timestamp, last_record_timestamp, last_record_id, _created_at, _updated_at FROM metadata LIMIT 1')
# # res = list(cur.fetchone())

# # print(res[7])
# # testResult = Metadata(_id=res[0], account_email=res[1], table_name=res[2], symbol=res[3], last_sync_timestamp=res[4], last_record_timestamp=res[5], last_record_id=res[6], created_at=res[7], updated_at=res[8])
# # print('created at - {}'.format(testResult.created_at))
# # testMd = Metadata(_id='74c0a004-1ab2-53f0-8509-362d919ba2e2', account_email='jhonDoe@mail.com', table_name='GetInfo', symbol='NA', last_sync_timestamp=1578638764000, last_record_timestamp=1578638962, last_record_id='NA')

# # testMd1 = testMd

# # datenow = datetime.utcnow()
# # print(datenow)

# # strdate = datetime.fromisoformat("2021-04-30 06:56:54.329417+00:00")
# # print(strdate)

# # print(testResult.created_at)
# # print(testMd.created_at is testResult.created_at)

# # m = Metadata.__fields__
# # fetch_fields = [m.get(c).alias or m.get(c).name for c in m]

# # print(fetch_fields)

# # print(os.getcwd())



# import files.tests_import as ti

# print(ti.public_func())

# def testing_nih():
#     print("func name {}".format(testing_nih.__name__))

# testing_nih()

# LOG_LEVEL_INFO = "INFO"
# LOG_LEVEL_DEBUG = "DEBUG"
# LOG_LEVEL_ERROR = "ERROR"
# LOG_LEVEL_WARNING = "WARNING    "
# LOG_LEVEL_CRITICAL = "CRITICAL"

# print(LOG_LEVEL_INFO)

# class TestArr:
#     ta_arr: []

# # ta = TestArr()
# # ta.ta_arr.append('testing')
# # ta.ta_arr.append('testing1')
# # ta.str_arr.append("test")
# # print(ta)


# def halo_raise() -> (str, BaseException):
#     try:
#         return 'Halo', None
#     except Exception as e:
#         return None, e
#     # return None, BaseException("testing raise for error " + halo_raise.__name__) 

# test, err = halo_raise()
# if err != None:
#     print(err)

# print(test)

# import model


# # testBook = model.Book()
# # testBook.id = 9
# print(model.Book)
# print(model.Book1)

# print(model.Book.__name__)

# def get_tuple(tup: namedtuple) -> (namedtuple, BaseException):
#     if tup != None:
#         return tup, None

#     return None, Exception("Tuple none")

# def check_book_tuple(tup: namedtuple) -> bool:
#     return tup == model.Book

# mod, err = get_tuple(None)
# if err != None:
#     print(err)

# if mod != None:
#     print(mod)

# test = [namedtuple]

# UserTransaction = namedtuple('user_transactions', [
#     'user_tx_id',
# 	'user_id',
# 	'paired_wallet',
# 	'tx_amount',
# 	'tx_direction',
# 	'fee_amount',
# 	'fee_label',
# 	'currency',
# 	'paired_currency',
# 	'status',
# 	'status_info',
# 	'tx_scope',
# 	'main_tx_id',
# 	'optional_message',
# 	'created_at',
# 	'updated_at',
# 	'exchange_rate',
# 	'paired_amount',
# 	'pairing_rate',
# 	'exa_tx_amount',
# 	'exa_fee_amount',
# 	'exa_paired_amount',
# ])

# TradingOrders = namedtuple('trading_orders', [
#     'order_id',
# 	'user_tx_id',
# 	'exchange_order_id',
# 	'exchange_id',
# 	'from_amount',
# 	'from_currency',
# 	'expected_amount',
# 	'to_currency',
# 	'actual_fee',
# 	'actual_from_amount',
# 	'actual_to_amount',
# 	'expected_fee',
# 	'fee_currency',
# 	'order_status',
# 	'created_at',
# 	'updated_at',
# 	'exa_from_amount',
# 	'exa_expected_fee',
# 	'exa_expected_amount',
# ])

# print(test)
# print(check_book_tuple(model.Book1))

# print(UserTransaction._fields)
# # column = str(UserTransaction._fields).replace('\', ')
# # testQuery = f"SELECT {str(UserTransaction._fields).replace('\', ')} FROM {UserTransaction.__name__}"

# # print(testQuery)

# import pytest

# def get_query_str():
# 	return 'SELECT 1+1 AS results'

# @pytest.mark.parametrize('name, query, expected', [
# 	('test func 0', get_query_str(), True),
# 	('test func 1', get_query_str(), True),
# 	('test func 2', get_query_str(), True)
# ])
# def test_func(name, query, expected):
# 	print(name)
# 	print('test - ' + query)
# 	print(expected)
	
import asyncio
from asyncio.events import AbstractEventLoop
import logging
import sys
from typing import Awaitable
import concurrent.futures

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_format = logging.StreamHandler(sys.stdout)
log_format.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'))

logger.addHandler(log_format)
logger.info("testing debug")

# import aioredis
# async def testing_redis_nih():
#     testing_redis = aioredis.from_url("redis://localhost:6379")
#     async with testing_redis.client() as cl:
#         await cl.get("testing")

def testing_str():
    return "testing"

async def testing_str_async(loop: AbstractEventLoop):
    exect = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    return await loop.run_in_executor(exect, testing_str)
    

loop = asyncio.get_event_loop()
result = loop.run_until_complete(testing_str_async(loop))
print(f"result loop - {result}")


