# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:13:19 2017

@author: P.Reeson
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = [1,2,3,4,5,6]

array1 = np.array(data1)
""" creates and np.array from data1 """
print(array1)
data2 = [[1,2,3,4],[5,5,6,8],[9,10,11,12]]
array2 = np.array(data2)
print(array2)

"""array.shape function returns x,y size of np.array"""
shape1 = array1.shape
shape2 = array2.shape
print("Shape of array 1 is:")
print(shape1)
print("Shape of array 2 is:")
print(shape2)

""" array.dtype returns array data type"""
print("array1 data type is ")
arrayd1 = array1.dtype
print(arrayd1)

"""can change array data type with array.astype(np.type)"""
float_array1 = array1.astype(np.float64)
float_arrayd1 = float_array1.dtype
print(float_arrayd1)

""" can automatically create arrays using functions"""
zeros = np.zeros((5,5))
print(zeros)
ones = np.ones((5,5))
print(ones)
ident = np.identity(10)
print(ident)

"""performing operatoions on arrays"""
add = zeros+6
print(add)
multiple = add*100
print(multiple)
many = multiple - add
print(many)
manytimes = many * many
print(manytimes)

""" Get slices or views of an array """
new = manytimes[2]
print(new)
new = manytimes[2,2]
print(new)

""" change specific slice of an array """
manytimes[2]=multiple[2]
print(manytimes)
manytimes[2,2]=999
print(manytimes)

""" indexing in 2D arrays """
print(manytimes[2,2])
print(manytimes[2][2])

""" in multi dimensional arrays incomplete calls return a lower 
dimesnion array with those starting indexes"""

data3d = [[1,2,3],[4,5,6],[7,8,9]]
array3d = np.array(data3d)
print(array3d)
cut = array3d[0]
print(cut)

"""generate random data arrays"""
random = np.random.randn(10,10) 
print(random)

""" 2D array slicing with different shapes"""
slice1 = zeros[2:,2:]
print(zeros)
print("///// slice 2:, 2:")
print(slice1)
slice2 = zeros[1:2,:2]
print("//////// slice 1:2, :2 //////////")
print(slice2)

""" indexing arrays with boolean operators """
names = np.array(['bob','steve','joe','tom','sue',])
newdata= np.random.randn(5,5)

print(names)
print(newdata)

""" Can get boolean value for array items """
namesboo = names=='bob'
print(namesboo)
namesNoboo = names!= 'bob'
print(namesNoboo)

""" The boolean array can be passed to index another array """
""" in this case the boolean for 'bob' passes 1st row """
print("///// 'bob' passed ////")
passed = newdata[names == 'bob']
print(passed)


print("///// NOT 'bob' passed ////")
passed2 = newdata[names != 'bob']
print(passed2)

""" Using multiple Boolean operators """

print("///// 'bob' and 'Joe' passed ////")
passed2 = newdata[(names == 'bob') | (names == 'joe')]
print(passed2)

""" Selecting data by Boolean indexing ALWAYS creates a copy """

""" Can set values with Boolean operators"""
setzero = np.random.randn(7,4)
print("new array.....")
print(setzero)
print("not set all <0 values to 0 with Boolean")
setzero[setzero <0] = 0
print(setzero)

""" Can set whole rows using 1D Boolean arrays"""
setzero[names != "joe"] = 12
print("reassigning rows using Boolean Arrays")
print(setzero)

""" Fancy Indexing using interger arrays """
print("Facncy indexing with interger arrays")
fancy_array = np.empty((8,4))
for i in range(8):
    fancy_array[i]=i
print(fancy_array)

""" can select out rows in any order by passing ndarray"""
print("can select out rows in any order by passing ndarray")
new_fancy = fancy_array[[4,3,0,6]]
print(new_fancy)

"""Can Transpose using T fucntion"""
print("Transpose using .T")
print(new_fancy.T)
print("Can do Dot product with arrays and T")
dotprod = np.dot(new_fancy.T,new_fancy.T)
print(dotprod)
























