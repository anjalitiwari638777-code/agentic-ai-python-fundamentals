import numpy as np
#method or functions to create numpy arrays 
#1
"""arr1=np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6]]);
#2
arr3=np.zeros((2,3));
#3
arr4 = np.ones((3,3));
#4
arr5 = np.identity(3);
#5
arr6 = np.arange(10,50,2);
#6
arr7 = np.linspace(10,20,10);
#7
arr8 = arr7.copy();
arr9 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# NUMPY ARRAY PROPERTIES AND ATTRIBUTES
# 1 . shape
print(arr9.shape); #(2,3)
#2.nDim
print(arr9.ndim); # give dimension ,3
#3 . size
print(arr9.size); # 8
print(arr9.itemsize); # 4
#4 .dtype
print(arr9.dtype);
#astype
print(arr9.astype('float'));
# numpy array vs pyhton lists
#faster,convenient,less memory
lista = range(100)
arr11 = np.arange(100)
import sys 
#less memory proof
print(sys.getsizeof(87)*len(lista));#2800
print(arr11.itemsize*arr11.size);#800
#faster proof
import time 
x = range(100000);
y = range(100000,200000)
start_time = time.time()
c=[(x,y)for x,y in zip(x,y)]
print(time.time()-start_time)
a=np.arange(100000)
b=np.arange(100000,200000)
start_time = time.time()
c=a+b;
print(time.time()-start_time)
#indexing iteration and slicing
arr12 = np.arange(24).reshape(6,4)
print(arr12)
print(arr12[2])# give second row
print(arr12[:,1:3])
print(arr12[2:4,1:3])
print(arr12[4:6,2:4])
for i in arr12:
    print(i)
for i in np.nditer(arr12):
    print(i)
#  numpy operation  
arr13 = np.array([1,2,3,4,5,6])
arr14 = np.array([4,5,6,7,8,9])  
print(arr13-arr14)  
print(arr13*arr14)
print(arr13*2)
print(arr14>3)
arr15 = np.arange(6).reshape(2,3)
arr16 = np.arange(6,12).reshape(3,2)
print(arr15.dot(arr16))
print(arr15.max())
print(arr16.min())
print(arr15.min(axis=0)) #min in every column
print(arr15.min(axis=1)) #min in every row
print(arr16.sum()) #sum of all element
print(arr16.sum(axis=0)) #sum of every colum wise
print(arr16.mean()) #calculate mean
print(arr15.std()) #standard deviation
print(np.sin(arr15)) #sine
print(np.median(arr15))#find median
print(np.exp(arr15)) #exponential
#reshaping numpy array
#ravel
print(arr16.ravel())# change the shape of a numpy array
#transpose
print(arr16.transpose())# row to column column to row
#stacking
arr17 =np.arange(12,18).reshape(2,3)
print(np.hstack((arr15,arr17)))#merge horizonatal both array
print(np.vstack((arr15,arr17)))#merge vertically 
#splitting
print(np.vsplit(arr15,2)) # divide vertically
print(np.hsplit(arr17,3)) #divide horizonatally
#fancy indexing
arr18=np.arange(24).reshape(6,4)
print(arr18[[0,2,4]])
#indexing using boolean arrays
arr=np.random.randint(low=1,high=100,size=20).reshape(4,5)
print(arr)
print(arr[(arr>50) & (arr%2!=0)])"""
#plotting graph using numpy
"""import matplotlib.pyplot as plt
x=np.linspace(-40,40,100)
#print(x)
#print(x.size)
y = np.sin(x)
plt.plot(x,y)
plt.show()
#broadcasting(opertions on different shape)
# if x=m and y=n operation will take place
a1=np.arange(8).reshape(2,4)
a2= np.arange(8,16).reshape(2,4)
print(a1+a2)
#if x=1 and y=n then slso operation will take place(same dimension)
a3=np.arange(3).reshape(1,3)
a4 = np.arange(12).reshape(4,3)
print(a3+a4)"""
#if x=1 and y!=n then also operations will not take place
#if x=1,y=1 then the operation will take place
#if they are of different dimension opertion will happen
#numpy functions
print(np.random.random())
print(np.random.seed(1))
print(np.random.random())
print(np.random.uniform(3,10))
a=np.random.randomint(1,10,2)
print(np.max(a))
print(np.argmax(a))




























