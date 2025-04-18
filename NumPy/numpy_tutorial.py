# -*- coding: utf-8 -*-
"""Numpy Tutorial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DbmPduvjMDv7TDqQeofH8sl8e0cAEZYS

NumPy - Numerical Python

Advantages of Numpy Arrays:
  1. Allow Several Mathematical Operations
  2. Faster Operations
"""

import numpy as np

"""List vs Numpy - Time Taken"""

from time import process_time

"""Time Taken by a List"""

python_list = [i for i in range(100000000)]
start_time = process_time()
python_list = [i + 5 for i in python_list]
end_time = process_time()

print(end_time - start_time)

"""Time Taken by NumPy Array"""

np_array = np.array([i for i in range(100000000)])
start_time = process_time()
np_array += 5
end_time = process_time()
print(end_time - start_time)

"""NumPy Arrays"""

#list
list1 = [1,2,3,4,5]
print(list1)
type(list1)

np_array1 = np.array([1,2,3,4,5])
print(np_array1)
type(np_array1)

"""Mathematical operation on a np Array"""

# in Python list
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print(list1 + list2) # Concatenate or joins 2 lists

a = np.random.randint(0,10,(3,3))
b = np.random.randint(11,20,(3,3))
print(a)
print(b)
print(a + b)
print(a - b)

a = np.random.randint(0,10,(3,3))
b = np.random.randint(11,20,(3,3))
print(a)
print(b)
print(np.sum(a + b))
print(np.add(a, b))

"""Array Manipulation"""

array = np.random.randint(0,10,(2, 3))
print(array)
print(array.shape)

print("TRANSPOSE")

trans = np.transpose(array) # Transpose or array.T
print(trans)
print(trans.shape)

# Reshaping a array
a = np.random.randint(0,10,(2,3))
print(a)
print(a.shape)

print("RESHAPE")

b = a.reshape(3, 2)
print(b)
print(b.shape)