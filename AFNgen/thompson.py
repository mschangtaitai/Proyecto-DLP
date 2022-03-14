
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
            afnList.append(AFN([i], [initialS, finalS], {i: [initialS,finalS]}, [initialS], [finalS]))
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

er = "a(a|b)*bab*"
afnList = []
mainAFN = AFN([], [], [], [], [])

getSigma(er, op, mainAFN)
createLeafs(er, op, afnList)
newEr = replaceConcat(er)

print(mainAFN.trans)
