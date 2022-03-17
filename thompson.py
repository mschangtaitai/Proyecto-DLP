
from subconjuntos import *
from thompsonModule import *
from graphAF import *

def thompson(er):
    afnList = []
    mainAFN = AF([], [], [], [], [])

    getSigma(er, mainAFN)
    createLeafs(er, afnList)
    if ("." not in er):
        newEr = replaceConcat(er)
    else:
        newEr = er
    newEr = inToPos(newEr)
    afnCont = 0
    afnStack = []

    for i in newEr:
        if (i not in op):
            afnStack.append(afnList[afnCont])
            afnCont += 1
        else:
            if(i == "*"):
                afn = kleene(afnStack.pop())
                afnStack.append(afn)

            elif(i == "+"):
                afn = plus(afnStack.pop())
                afnStack.append(afn)

            elif(i == "."):
                afn2 = afnStack.pop()
                afn1 = afnStack.pop()

                afn = concat(afn1,afn2)
                afnStack.append(afn)

            elif(i == "|"):
                afn2 = afnStack.pop()
                afn1 = afnStack.pop()

                afn = opor(afn1,afn2)
                afnStack.append(afn)
    
    return afnStack[0]
