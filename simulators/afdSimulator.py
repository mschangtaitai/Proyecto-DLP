from module import *

def afdSimulator(afd, w):
    s = afd.start
    for i in w:
        s = move(s,i,afd.trans)
    
    if s[0] in afd.finals:
        return True
    return False

#Area de pruebas

testAFD = AF(["1", "2", "3", "4", "5"], ["a", "b"], [
    ["1", "a", "2"],
    ["1", "b", "3"],
    ["2", "a", "2"],
    ["2", "b", "4"],
    ["3", "a", "2"],
    ["3", "b", "3"],
    ["4", "a", "2"],
    ["4", "b", "5"],
    ["5", "a", "2"],
    ["5", "b", "3"]
    ], ["1"], ["5"])

cadena = "abbaabb"

result = afdSimulator(testAFD,cadena)
print(result)
