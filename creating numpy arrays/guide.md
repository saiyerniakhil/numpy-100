# Creating arrays with NumPy

A NumPy array can be created using array() function from the NumPy module.

## Creating arrays using arange() method

What does an arange() function do?
arange (not arrange!) a_range, which is self explanatory, creates a numpy array with a range from 0 to 10(excluding 10).

syntax:
numpy.arange(start,stop,step)

## Creating NumPy arrays using zeros() and ones()

What does a ones(n) do?

Create a one dimensional array with n ones

What does a zeros(n) do?

Create a one-dimensional array with n zeros

How to create two dimensional arrays of zeros and ones?

```twoDimOnes = np.ones((5,3))```


## Creating an array using numpy.full()

What does numpy.full(n,(m,..),constant) do?

Create a 2d array with a constant number

## Creating an array with linspace() 

What does linspace(start,stop,n) do?

linspace does generate an one-dim array with 'n' elements 
between start and stop values.

## What is an Identity Matrix?
An identity matrix is a two-dimesional matric with its diagonal matrix contaning ones

example:

A two-dim identity matrix: 
```
                           [1   0]

                           [0  1 ]  
```

What does eye(m,[n,..])  do?

Create a 2d identity matrix of spedified no. of rows and cols.

## Creating an array  containing random integers using NumPy.random.rand()

What does NumPy.random.rand(m,[n,..]) do ?

Generates a one/two dimensional array of random numbers 


