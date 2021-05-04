from pydantic import BaseModel
from datetime import datetime
import psycopg2
import os
class EntityTest(BaseModel):
    name: str

test = EntityTest(name="test1")
test1 = EntityTest(name="test1")
print(test.__class__.__name__)

print("testing name {}".format(__name__))

print(test == test1)

import data_type.str_class as strc

strc.print_str()

from data_type.str_class import Metadata

halo = Metadata(_id='74c0a004-1ab2-53f0-8509-362d919ba2e2', account_email='jhonDoe@mail.com', table_name='GetInfo', symbol='NA', last_sync_timestamp=1578638764000, last_record_timestamp=1578638962, last_record_id='NA')
# print(halo.__fields__)
# print(halo.created_at)

testingArry = [1,2,3]
copyTest = []

for item in testingArry:
    copyTest.append(item)

print(copyTest)

# testDbParam = dict(host='localhost', port=5432, user='postgres', password='postgres', dbname='indodax_agent')
# print(**testDbParam)
# conn = psycopg2.connect(dsn="host='localhost' port=5432 user='postgres' password='postgres' dbname='indodax_agent'")

# cur = conn.cursor()

# cur.execute('SELECT _id, account_email, table_name, symbol, last_sync_timestamp, last_record_timestamp, last_record_id, _created_at, _updated_at FROM metadata LIMIT 1')
# res = list(cur.fetchone())

# print(res[7])
# testResult = Metadata(_id=res[0], account_email=res[1], table_name=res[2], symbol=res[3], last_sync_timestamp=res[4], last_record_timestamp=res[5], last_record_id=res[6], created_at=res[7], updated_at=res[8])
# print('created at - {}'.format(testResult.created_at))
# testMd = Metadata(_id='74c0a004-1ab2-53f0-8509-362d919ba2e2', account_email='jhonDoe@mail.com', table_name='GetInfo', symbol='NA', last_sync_timestamp=1578638764000, last_record_timestamp=1578638962, last_record_id='NA')

# testMd1 = testMd

# datenow = datetime.utcnow()
# print(datenow)

# strdate = datetime.fromisoformat("2021-04-30 06:56:54.329417+00:00")
# print(strdate)

# print(testResult.created_at)
# print(testMd.created_at is testResult.created_at)

# m = Metadata.__fields__
# fetch_fields = [m.get(c).alias or m.get(c).name for c in m]

# print(fetch_fields)

# print(os.getcwd())



import files.tests_import as ti

print(ti.public_func())