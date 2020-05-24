# coding=<encoding name>

from sys import argv

param1, param2, param3, param4 = argv

print("Script: ", param1)
print("????????? ? ?????: ", param2)
print("?????? ? ???: ", param3)
print("??????: ", param4)

def salary(param2, param3, param4):
    return float(param2) * float(param3) + float(param4)

print(salary(param2, param3, param4))

