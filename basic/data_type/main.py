import string
from operation import Operate
from pydantic import BaseModel

o = Operate()
o.printout('testing aja')
res = o.add([1,2,3,4,5])
print("result - {}".format(res))

strArr = ["halo", 1, 0.65, 1e10]
print(strArr)
print(*strArr)

class Entity(BaseModel):
    ID: int
    name: str
    desc: str

testEntity = Entity(ID=1, name="halo", desc="desc halo")
print(testEntity)
print(string.TestString)

