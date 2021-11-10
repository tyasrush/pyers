from datetime import datetime, tzinfo
import time
from dateutil.parser import parse

dts = '2021-11-06T08:41:25.916113015Z'
print(f"date : {len(dts)} date (-7): {len(dts[:-7])}")
str_d = dts[0:-(len(dts)-23)]
print(str(str_d))
tmp = datetime.fromisoformat(str_d).timestamp()
print("dt tmp: " + str(tmp))
pt = parse(dts)
print(pt.timestamp())