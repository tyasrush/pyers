from operation import Operate

o = Operate()
o.printout('testing aja')
res = o.add([1,2,3,4,5])
print("result - {}".format(res))

strArr = ["halo", 1, 0.65, 1e10]
print(strArr)
print(*strArr)