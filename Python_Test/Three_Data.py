#coding: utf-8
import numpy as np
import random
import os

os.system('clear')

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

def aleaInt(n):
    return random.randint(0, n)

def proba2answer(trainedData):
    trainedData = np.around(trainedData, 0)
    return nonlin(trainedData)

def generateMatrix(row, columns):
	laListe = []
	lesOccurrences = []
	for i in range(row):
		laListe.append([])
		for j in range(columns):
			laListe[i].append(aleaInt(3))
		print laListe
	for i in laListe:
		for j in i:
			lesOccurrences.append(i.count(j))
	for i in range(len(lesOccurrences)):
#		for j in range(len(lesOccurrences[i])):
		print "Valeur", i, ": ", lesOccurrences[i], "occurrences"
	return laListe


X = np.array(generateMatrix(4, 3))

# input dataset
#X = np.array([  [aleaInt(), aleaInt(), aleaInt()],
#                [aleaInt(), aleaInt(), aleaInt()],
#                [aleaInt(), aleaInt(), aleaInt()],
#                [aleaInt(), aleaInt(), aleaInt()] ])

print "Input matrix: "
print X

# output dataset            
y = np.array([[aleaInt(3), aleaInt(3), aleaInt(3), aleaInt(3)]]).T

print "Output matrix: "
print y, "\n"

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(100000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1
    

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)

print "Output After Training:"
print l1
print "Résulats obtenus:"
print np.dot(l0,syn0)
print "Réponse fournie: "
print proba2answer(l1)
