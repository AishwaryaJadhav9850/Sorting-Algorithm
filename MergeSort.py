# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:56:39 2020

@author: SUPERNOVA2813

External Sorting
worst case id O(N log N)
Based on recursive algorithm 

"""

def MergeSort(array,low,high):
    if(low<high):
        middle=(low+high)//2
        MergeSort(array,low,middle) #Lower half
        MergeSort(array,middle+1,high) # Upper half
        Merge(array,low,middle,high) # Merge Lower and upper half
        
    
def Merge(array,low,mid,high):
    i=low
    j=mid+1
    k=0
    l=[0 for p in range(high+1)] #new list to temporary store the merged list
    #Compare the lower half and upper half and copy smaller element into new temporary list
    while i<=mid and j<=high:
        if array[i]<array[j]:
            l[k]=array[i]
            k+=1
            i+=1            
        else:
            l[k]=array[j]
            k+=1
            j+=1
    #if list 1 is exhausted, merge the remaining list 2        
    while(i<=mid):
        l[k]=array[i]
        k+=1
        i+=1
    while(j<=high):
        l[k]=array[j]
        k+=1
        j+=1
    
    #copy back data to the original array form the temporary array
    p=0
    for i in range(low,high+1):
        array[i]=l[p]
        p+=1
    
    
array=[int(x) for x in input("Enter the array for sorting using Merge Sort:").split(" ")]
lenth=len(array)-1
MergeSort(array,0,lenth)
print("Sorted array is : ",array)