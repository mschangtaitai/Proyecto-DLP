
from resources import *

def inToPos(infix):
    # Curly braces = dictionary
    # *, +, and ? are repetition operators. They take precedence over concatenation and alternation operators
    # * = Zero or more
    # + = One or more
    # ? = Zero or one
    # . = Concatenation
    # | =  Alternation
    specials = {'?': 70, '+': 60, '*': 50, '.': 40, '|': 30}

    pofix = ""
    stack = ""

    # Loop through the string one character at a time
    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[:-1]
            # Remove '(' from stack
            stack = stack[:-1]
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        else:
            pofix = pofix + c

    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]
        
    return pofix


def concat(afn1,afn2):
    mutualState = afn1.finals[0] + afn2.start[0]
    states = list(set(afn1.states + afn2.states + [mutualState]) - set(afn1.finals) - set(afn2.start))
    sigma = afn1.sigma + [i for i in afn2.sigma if i not in afn1.sigma]
    trans = afn1.trans + afn2.trans
    for tran in trans:
        for i in tran:
            if((i == afn1.finals[0]) or (i == afn2.start[0])):
                tran[tran.index(i)] = mutualState
    
    return AF(states, sigma, trans, afn1.start, afn2.finals)

def opor(afn1,afn2):
    newStart = afn1.start[0] + afn2.start[0]
    newFinal = afn1.finals[0] + afn2.finals[0]
    states = afn1.states + afn2.states + [newStart] + [newFinal]
    sigma = afn1.sigma + [i for i in afn2.sigma if i not in afn1.sigma]
    trans = afn1.trans + afn2.trans
    trans.append([newStart,"E",afn1.start[0]])
    trans.append([newStart,"E",afn2.start[0]])
    trans.append([afn1.finals[0],"E",newFinal])
    trans.append([afn2.finals[0],"E",newFinal])

    return AF(states,sigma,trans,[newStart],[newFinal])

def kleene(afn):
    newStart = "new" + afn.start[0]
    newFinal = "new" + afn.finals[0]
    states = afn.states + [newStart] + [newFinal]
    trans = afn.trans
    

    trans.append([newStart,"E",afn.start[0]])
    trans.append([afn.finals[0],"E",newFinal])
    trans.append([afn.finals[0],"E",afn.start[0]])
    trans.append([newStart,"E",newFinal])

    return AF(states,afn.sigma,trans,[newStart],[newFinal])

def plus(afn):
    return concat(kleene(afn),afn)


