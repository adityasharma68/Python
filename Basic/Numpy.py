##Python Numpy Arrays

#NumPy is general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.

## What is an Array?
#An array is data structure that stores values of some data type. In Python, this is the main difference between arrays and list. While lists can store values of different data types, arrays in NumPy can only store values of the same data type.

## import the numpy package
import numpy as np

lst=[1,2,3,4,5]

np.array(lst)  #Convert the list to a numpy array
# print(np.array(lst))  #Output: [1 2 3 4 5]

# print(type(np.array(lst)) ) #Output: <class 'numpy.ndarray'>

#Creating a 2-D array
arr_2d = np.array([[1,2,3],[4,5,6]])
# print(arr_2d)

#Creating an 3-D array
# lst1=[1,2,3,4,5,6]
# lst2=[7,8,9,10,11,12]
# lst3=[13,14,15,16,17,18]

# arr_3d = np.array([lst1,lst2,lst3])
# print(arr_3d)

# print(arr_3d.shape)  #Output: (3, 6) It means 3 rows and 6 columns

#Indexing

# print(arr_3d[0,1])  #Output: 2 arr_3d[0,1] means first row and second column
# print(arr_3d[2,4])  #Output: 17 arr_3d[2,4] means third row and fifth column


arr01 = np.array([1,2,3,4,5])

print(arr01[4]) #Output: 5

print(arr01[1:3]) #Output: [2 3] Slicing means getting a subset of array
print(arr01[1:4]) #Output: [2 3 4]
print(arr01[-1]) #Output: 5 Negative indexing means start from the end
print(arr01[:-1]) #Output: it means skip the last element [1 2 3 4]
print(arr01[::-1]) #Output: it means reverse the array [5 4 3 2 1]
print(arr01[::-2]) #Output: it means reverse the array and get every second element [5 3 1]


## for multiple dimensions
lst1=[1,2,3,4,5,6]
lst2=[7,8,9,10,11,12]
lst3=[13,14,15,16,17,18]

arr_3d = np.array([lst1,lst2,lst3])

print(arr_3d[:,1]) #Output: [ 2  8 14] It means get all rows and second column, it indexing in the form of arr_3d[rows, columns] and ":" it means all rows or all columns

print(arr_3d[1:,2:4]) # arr_3d[1:,2:4]  in this 1 means start from second row to the end and 2:4 means get third and fourth column Output: [[ 9 10]
                                        # [15 16]]

#creating a matrix from 3d array [[1 2 3][16 17 18]]
print(arr_3d[[0,2],:3]) #Output: [[ 1  2  3]
                        #         [13 14 15]] In this [0,2] means get first and third row and :3 means get first three columns



## Array reshape
# arr_3d.reshape(2,3,3)  #Output: reshape the array to 2 matrices with 3 rows and 3 columns

##mechanism to create arrays

arr03 = np.arange(0,10,1).reshape(2,5)  #Output: create an array from 0 to 9 with step 1 and reshape it to 2 rows and 5 columns  
print(arr03)

arr4 = np.ones((3,4))  #Output: create an array of ones with 3 rows and 4 columns
print(arr4)

arr5 = np.zeros((2,3))  #Output: create an array of zeros with 2 rows and 3 columns
print(arr5)

#diff btwn zeros and zeros_like


#random randiants 

arr6 = np.random.randint(10,50)
print(arr6)  #Output: create a random integer between 10 and 50