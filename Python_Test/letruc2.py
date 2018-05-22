#coding: utf-8
from string import _float

class Civilization:
	def __init__(self, population=[]):
		population


import random

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

#Nombre aléatoire entre x et y
def alea(x, y):
	leNombre = random.randint(x, y)
	return leNombre 

def afficher(nombre):
	if nombre < 1000000:
		print nombre
		return
	if nombre > 1000000 and nombre < 1000000000:
		nombre = nombre*(10**-6)
		nombre = str(nombre)
		leNombre = nombre.split(".")
		print leNombre[0], "m"
		return
	if nombre > 1000000000:
		print nombre
		nombre = nombre*(10**-9)
		nombre = str(nombre)
		leNombre = nombre.split(".")
		print leNombre[0], "G"




resultats = []

for i in range(9):
	resultats.append(int(alea(120000000, 30000000000)))

intervalle = 9
i = 0
j = 0

print resultats
print ""
print ""

while True:
	if len(resultats)==3:
		break
	somme = resultats[i] + resultats[i+1] + resultats[i+2]
	resultats.pop(i+1)
	resultats.pop(i+1)
	resultats[j] = somme/3
	i += 1
	j += 1
		


print ""
for i in resultats:
	afficher(i)
