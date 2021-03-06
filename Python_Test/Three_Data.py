#coding: utf-8
import numpy as np
import random



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
			laListe[i].append(aleaInt(1))
			print laListe
	print ""
	return laListe


# X = np.array(generateMatrix(4, 3))

# input dataset
X = np.array([  [0, 1, 0],
				[0, 1, 0],
				[1, 1, 0],
				[1, 1, 1] ])

print "Input matrix: "
print X

# output dataset			
y = np.array([[0, 0, 1, 1]]).T

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
print "Réponse fournie: "
print nonlin(l1, True)
