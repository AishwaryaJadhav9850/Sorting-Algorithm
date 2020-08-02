# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 20:56:31 2020

@author: SUPERNOVA2813
"""

def ShellSort(array):
    l=len(array)
    grp=l//2 # this is the group within the array
    
    i=0
    j=grp
    
    # Do sorting till the group is greater than 0
    #compare elements between groups and swap if element form right group is greater than element in left group
    while(grp>0):
        while(i<j and j!=l):
            if array[i]>array[j]:
                temp=array[i]
                array[i]=array[j]
                array[j]=temp            
            i+=1
            j+=1               
        if j==l: # AFter pass is completed again decrease the group size by half
            grp=grp//2
            i=0
            j=grp

    
    
    
    
array=[int(x) for x in input("Enter the array for sorting using Shell Sort:").split(" ")]
ShellSort(array)
print("Sorted array is : ",array)