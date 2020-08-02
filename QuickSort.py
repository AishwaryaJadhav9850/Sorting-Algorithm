# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 23:06:47 2020

@author: SUPERNOVA2813
Inplace sorting algo
unstable
worst case : O(n^2)
average case : O(nLogn)

"""

def QuickSort(array,low,high):    
    if(low>=high):
        return
    pivot=array[low] # Make the 1st element as Pivot
    i=low+1 # Pointer 2nd element for lower part
    j=high #Pointer at the end of array, last element for upper part
    while True: #Basic condition
        while i<=j and array[j]>=pivot: # if element of upper part already larger, decrement
            j-=1
        while i<=j and array[i]<=pivot: #if element of lower part already smaller, only increament
            i+=1
        
        if i<=j: # Search for smaller element than pivot and larger element than pivot
            array[i],array[j]=array[j],array[i]  # Swap the smaller and Larger element
        else:
            break
        
    #if array[i]<pivot: # when i and j intersect, swap the pivot with the ith element of the intersection
    array[low],array[j]=array[j],array[low]
 
    QuickSort(array,low,j-1)  # Quick sort the lower part - left of Pivot
    QuickSort(array,j+1,high) # Quick sort the upper part - Right of Pivot
        
     
    
array=[int(x) for x in input("Enter the array for sorting using Quick Sort:").split(" ")]
lenth=len(array)-1
QuickSort(array,0,lenth)
print("Sorted array is : ",array)