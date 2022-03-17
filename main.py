from thompson import *
from subconjuntos import *
from minizacion import *
from graphAF import *
from afdSimulator import *
from afnSimulator import *

er = input("Ingrese la expresion regular: ")
w = input("Ingrese la cadena que desea verificar: ")

afn = thompson(er)
graphAF(afn, "AFN")
afnTest = afnSimulator(afn,w)
print("Cumple con el AFN: " + str(afnTest))

afd = subconjuntos(afn)
graphAF(afd, "AFD")
afdTest = afdSimulator(afd,w)
print("Cumple con el AFD: " + str(afdTest))

afdmin = minAFD(afd)
graphAF(afdmin, "AFDmin")
afdminTest = afdSimulator(afdmin,w)
print("Cumple con el AFD minimizado: " + str(afdminTest))
