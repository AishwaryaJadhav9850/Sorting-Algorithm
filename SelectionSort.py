# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:13:08 2020

@author: SUPERNOVA2813

Time Complexity worst case O(n^2) 
Stable sorting alogrithmn
inplace sorting
works nicely for small set of data
No additional storage is required

"""

def SelectionSort(array):
    for i in range(len(array)):
        temp=array[i]
        index=i
        #swap the ith value of array with the smallest element from the remaining list
        for j in range(i+1,len(array)): #loop over remaining list
            if array[j] < temp: #search for smallest elememt
                temp=array[j]
                index=j
        if array[i]>temp: #swap the smallest element with the element in the sorted array
            array[index]=array[i]
            array[i]=temp                        
        print(array) #array status after each pass
                

array=[int(x) for x in input("Enter the array for sorting using Selection Sort:").split(" ")]
SelectionSort(array)
print("Sorted array is : ",array)