from thompson import *
from subconjuntos import *
from graphAF import *
from afdSimulator import *
from afnSimulator import *

er = input("Ingrese la expresion regular: ")
w = input("Ingrese la cadena que desea verificar: ")

afn = thompson(er)
afd = subconjuntos(afn)

graphAF(afn, "AFN")
graphAF(afd, "AFD")

afnTest = afnSimulator(afn,w)
afdTest = afdSimulator(afd,w)

print("Cumple con el AFN: " + str(afnTest))
print("Cumple con el AFD: " + str(afdTest))