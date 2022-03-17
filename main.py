import time
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
start_time = time.time()
afnTest = afnSimulator(afn,w)
final_time = time.time() - start_time
print("Cumple con el AFN: " + str(afnTest))
print("Tiempo de validacion: " + str(final_time), end = "\n\n")

afd = subconjuntos(afn)
graphAF(afd, "AFD")
start_time = time.time()
afdTest = afdSimulator(afd,w)
final_time = time.time() - start_time
print("Cumple con el AFD: " + str(afdTest))
print("Tiempo de validacion: " + str(final_time), end = "\n\n")

afdmin = minAFD(afd)
graphAF(afdmin, "AFDmin")
start_time = time.time()
afdminTest = afdSimulator(afdmin,w)
final_time = time.time() - start_time
print("Cumple con el AFD minimizado: " + str(afdminTest))
print("Tiempo de validacion: " + str(final_time), end = "\n\n")
