# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:49:48 2020

@author: SUPERNOVA2813

Time Complexity worst case O(n^2) best case O(n)
Stable sorting alogrithmn
inplace sorting
works nicely for small set of data
No additional storage is required
"""

def InsertionSort(array):    
    for i in range(1,len(array)):
        if array[i]<array[i-1]: # if element is smaller than previous element
            #lower part of the list will be sorted at any time
            for j in range(i-1,-1,-1): # bactrace to insert the element in appropriate place
                if array[j]>array[j+1]:#swap if element is smaller than previous element
                    temp=array[j]
                    array[j]=array[j+1]
                    array[j+1]=temp
            print(array)
                


    
    
    
array=[int(x) for x in input("Enter the array for sorting using Insertion Sort:").split(" ")]
InsertionSort(array)
print("Sorted array is : ",array)