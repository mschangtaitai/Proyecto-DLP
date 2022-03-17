
from module import *

def afnSimulator(afn, w):
    s = eClosure(afn.start,afn.trans)
    for i in w:
        s = eClosure(move(s,i,afn.trans),afn.trans)
    
    for i in s:
        if i in afn.finals:
            return True
    return False

#Area de pruebas

# (a|b)*abb
# testAFN = AF(["0","1","2","3","4","5","6","7","8","9","10"], ["a","b"], [
#     ["0","E","1"],
#     ["0","E","7"],
#     ["1","E","2"],
#     ["1","E","4"],
#     ["2","a","3"],
#     ["3","E","6"],
#     ["4","b","5"],
#     ["5","E","6"],
#     ["6","E","1"],
#     ["6","E","7"],
#     ["7","a","8"],
#     ["8","b","9"],
#     ["9","b","10"],
#     ], ["0"], ["10"])

# cadena = "abababb"

# result = afnSimulator(testAFN,cadena)
# print(result)
