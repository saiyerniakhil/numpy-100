# Indexing / Selecting NumPy arrays

## Integer Array Indexing
----

## How to access nth element of a numpy array?

let sampleArr is a numpy array containing n elements. 5th element of the array can be accessed using ```sampleArr[5]```

## How to draw out / select a sub-array from a given array?

let a, be a numpy array 
```
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
 ```
 How select the following sub array ?
 ```
 [[3 4]
 [7 8]]
 ```
 This will do that  ```a[:2, 2:4]```
 
 Explanation:

 it selects first two rows 0,1 (excluding 2) and cols 2,3 (excluding 4) like general lists in the python

 ## Boolean Array Indexing
 ----

 Indexing a numpy array based on boolean operations.

 let a, be a numpy array like 
 ```
 [[3 4]
 [7 8]]
 ```
 when we perform boolean indexing like this   ``` b = (a > 2) ```

 Then the result is ike this - 
 ```
 [[False False]
 [ True  True]]
 ```

 Explanation:

 The the above operation compares all elements of the array ```a``` and return ```True``` / ```False``` if the corresponding element is greater it returns ```True``` else ```False```.
 

