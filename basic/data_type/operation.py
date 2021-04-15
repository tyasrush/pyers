class Operate():

    def printout(self, strVal: str):
        print(strVal)

    def add(self, values: [int]):
        result = 0
        for v in values: result = result + v
        return result
