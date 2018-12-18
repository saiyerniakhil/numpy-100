import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.array([[4, 5, 6, 7], [2, 5, 6, 3], [4, 8, 9, 1]])

# arithmetic operation
c = a + b
d = a - b
e = a * b
f = a / b

#scientific operations

c = np.log(a)  # find logarithm of all elements of the array
d = np.sqrt(a)  # find square root of all elements of the array
e = np.std(a)  # find standard deviation of the array 
f = np.sin(a)  # find sin of all elemets of the array
g = np.cos(a)   # find cos of all elemets of the array
h = np.sum(a)   # Find sum of all elemets of the array

#Special sum operations

a.sum() #Finds sum of all elements of an array
a.sum(axis=0) #finds sum of elements across columns in the array
a.sum(axis=1)  # finds sum of elements across rows in the array



