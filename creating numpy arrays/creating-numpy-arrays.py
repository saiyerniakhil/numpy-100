import numpy as np


numpyArray = np.arange(10)
#print(numpyArray)

numpyArray1 = np.arange(1,10,2)
#print(numpyArray)

numpyArray2 = np.arange(0,11,2)
#print(numpyArray2)


arrayOfOnes = np.ones(5)
#print(arrayOfOnes)


arrayOfZeros = np.zeros(5)
#print(arrayOfZeros)

#How to create two dimensional arrays of zeros and ones?
twoDimOnes = np.ones((5,3))
#print(twoDimOnes)


constArr = np.full((2, 5), 10)  # create an array with 2 rows and 5 cols
#print(constArr)


evenSpaced = np.linspace(2,5,10)
#print(evenSpaced)


twoDimIden = np.eye(3)
#print(twoDimIden)


randomMatrix = np.random.rand(5,2) #Generates a 2d array of 5 rows and 2 cols
#print(randomMatrix) 



