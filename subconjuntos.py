
from module import *
import graphviz

def subconjuntos(afn):

    dStates = [eClosure(afn.start, afn.trans)]
    dTrans = []
    dFinals = []

    for state in dStates:
        for sign in afn.sigma:
            u = eClosure(move(state,sign,afn.trans),afn.trans)
            flag = True
            for s in dStates:
                if(set(u) == set(s)):
                    flag = False
                    index = dStates.index(s)
            if(flag):
                dStates.append(u)
                for i in u:
                    if ((i in afn.finals) and (str(len(dStates)) not in dFinals)):
                        dFinals.append(str(len(dStates)))

                dTrans.append([str(dStates.index(state) + 1),sign,str(len(dStates))])
            else:
                dTrans.append([str(dStates.index(state) + 1),sign,str(index + 1)])
    
    finalStates = []
    for i in range(len(dStates)):
        finalStates.append(str(i+1))
    
    return(AF(finalStates,afn.sigma,dTrans,["1"],dFinals))

#Area de pruebas

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

# result = subconjuntos(testAFN)

# print(result.states)
# print(result.sigma)
# print(result.trans)
# print(result.start)
# print(result.finals)

# f = graphviz.Digraph('finite_state_machine', filename='fsm')
# f.attr(rankdir='LR', size='20')

# f.attr('node', shape='doublecircle')
# for i in result.finals:
#     print(i)
#     f.node(i)
    
# f.attr('node', shape='circle')
# for i in result.trans:
#     f.edge(i[0], i[2], label=i[1])

# f.view()
