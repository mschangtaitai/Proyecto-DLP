
from module import *

def minAFD(afd):
    part = [item for item in afd.states if item not in afd.finals]

    partitions = [part, afd.finals]
    states = afd.states.copy()
    sigma = afd.sigma.copy()
    trans = afd.trans.copy()
    start = afd.start.copy()
    finals = afd.finals.copy()

    added = True
    while(added):
        added = False
        for i in partitions:
            if (len(i) > 1):
                for s in sigma:
                    newPart = []
                    target = -1
                    for j in i:
                        result = move(j,s,trans)
                        if(len(result) > 0):
                            for part in partitions:
                                if (result[0] in part):
                                    if ((target == -1) or (target == partitions.index(part))):
                                        target = partitions.index(part)
                                    
                                    else:
                                        newPart.append(j)
                    
                    if(len(newPart)>0):
                        for part in partitions:
                            partitions[partitions.index(part)] = list(set(part) - set(newPart))
                        partitions.append(newPart)
                        added = True

    for part in partitions:
        removed = []
        for state in part:
            if part.index(state) > 0:
                states.remove(state)
                if state in start:
                    start.remove(state)
                    start.append(part[0])
                if state in finals:
                    finals.remove(state)
                    finals.append(part[0])


            for tran in trans:
                for k in tran:
                    if k == state:
                        trans[trans.index(tran)][tran.index(k)] = part[0]

    newTrans = []

    for i in trans:
        if i not in newTrans:
            newTrans.append(i)

    return AF(states,sigma,newTrans,start,finals)

# Area de pruebas

# afd = AF(["0","1","2","3","4","5","6"], ["a","b"],[
#     ["0", "a", "0"],
#     ["0", "b", "4"],
#     ["1", "a", "1"],
#     ["1", "b", "2"],
#     ["2", "a", "2"],
#     ["2", "b", "2"],
#     ["3", "a", "3"],
#     ["3", "b", "2"],
#     ["4", "a", "0"],
#     ["4", "b", "2"],
#     ["5", "a", "6"],
#     ["6", "b", "5"],
# ], ["0"], ["2","6"])

# result = minAFD(afd)

# print(result.states)
# print(result.sigma)
# print(result.trans)
# print(result.start)
# print(result.finals)