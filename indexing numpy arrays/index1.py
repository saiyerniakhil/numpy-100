import numpy as np

#integer array indexing
sampleArr = np.arange(10)

#print(sampleArr)
#print(sampleArr[1])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[:2, 2:4])

#boolean array indexing

b = np.array([[0,2],[4,7]])

c = (b > 2)
print(c)

