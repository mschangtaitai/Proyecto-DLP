
from thompsonModule import *
import graphviz

op = ["(", "*", "+", "|", ".", ")"]

class AFN:
    def __init__(self, sigma, states, trans, start, finals):
        self.sigma = sigma
        self.states = states
        self.trans = trans
        self.start = start
        self.finals = finals


def getSigma(er, op, mainAFN):
    for i in er:
        if (op.__contains__(i) == False):
            if(mainAFN.sigma.__contains__(i) == False):
                mainAFN.sigma.append(i)
    return mainAFN

def createLeafs(er, op, afnList):
    num = 0
    for i in er:
        if (op.__contains__(i) == False):
            initialS = "i" + i + str(num)
            finalS = "f" + i + str(num)
            afnList.append(AFN([i], [initialS, finalS], [[initialS,i,finalS]], [initialS], [finalS]))
            num += 1

def replaceConcat(er):
    newEr = er
    prev = ""
    cont = 0
    for i in er:
        if ((i == ")") or (i == "|") or (prev == "|") or (prev == "(") or (prev == "") or (i =="*") or (i =="+")) == False:
            newEr = newEr[:cont] + "." + newEr[cont:]
            cont += 1
        cont += 1
        prev = i
    
    return newEr

def operateLeafs():
    print("operating leafs")

#Area de pruebas

er = "a(a|b)*bab*"
afnList = []
mainAFN = AFN([], [], [], [], [])

getSigma(er, op, mainAFN)
createLeafs(er, op, afnList)
newEr = replaceConcat(er)

# print(mainAFN.sigma)
# for i in afnList:
#     print("******************")
#     print(i.states)
#     print(i.sigma)
#     print(i.trans)
#     print(i.start)
#     print(i.finals)

testAFN = AF(["0","1","2","3","4","5","6","7","8","9","10"], ["a","b"], [
    ["0","E","1"],
    ["0","E","7"],
    ["1","E","2"],
    ["1","E","4"],
    ["2","a","3"],
    ["3","E","6"],
    ["4","b","5"],
    ["5","E","6"],
    ["6","E","1"],
    ["6","E","7"],
    ["7","a","8"],
    ["8","b","9"],
    ["9","b","10"],
    ["9","E","3"],
    ], ["0"], ["10"])

# result = opor(afnList[-1],afnList[-2])
# result = opor(afnList[-1],testAFN)
result = (afnList[-1])
# print(result.states)
# print(result.sigma)
# print(result.trans)
# print(result.start)
# print(result.finals)

f = graphviz.Digraph('finite_state_machine', filename='fsm')
f.attr(rankdir='LR', size='20')

f.attr('node', shape='doublecircle')
for i in result.finals:
    print(i)
    f.node(i)

f.attr('node', shape='circle')
for i in result.trans:
    f.edge(i[0], i[2], label=i[1])

f.view()

