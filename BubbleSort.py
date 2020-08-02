# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:15:42 2020

@author: SUPERNOVA2813

Time Complexity worst case O(n^2) best case O(n)
Stable sorting alogrithmn
inplace sorting
works nicely for small set of data
No additional storage is required

"""

    
def BubbleSort():
    if(len(array)<0):
        print("Array is empty!")
        return
    flag=0    
    while(flag==0):        
        flag=1 #flag to break the loop if the array is sorted
        for i in range(len(array)-1):
            if array[i]>array[i+1]: #comparing element and swapping
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
                flag=0 
     
            
array=[int(x) for x in input("Enter the array for sorting:").split(" ")]
BubbleSort()
print("Sorted array is : ",array)
