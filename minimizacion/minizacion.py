
from resources import *

testAFN = AF(["0","1","2","3","4","5","6"], ["a","b"],[
    ["0", "a", "0"],
    ["0", "b", "4"],
    ["1", "a", "1"],
    ["1", "b", "2"],
    ["2", "a", "2"],
    ["2", "b", "2"],
    ["3", "a", "3"],
    ["3", "b", "2"],
    ["4", "a", "0"],
    ["4", "b", "2"],
    ["5", "a", "6"],
    ["6", "b", "5"],
], ["0"], ["2","6"])

part = [item for item in testAFN.states if item not in testAFN.finals]

partitions = [part, testAFN.finals]

print(partitions)

for i in partitions:
    print("Partition: ")
    target = -1
    if (len(i) > 1):
        for s in testAFN.sigma:
            for j in i:
                print("**************")
                result = move(j,s,testAFN.trans)
                print(j,s,result)
                if(len(result) > 0):
                    for part in partitions:
                        if (result[0] in part):
                            print("Im on part: ", part)

print("test")
