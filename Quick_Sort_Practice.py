#One of the fastest sorting algorithms

#Worst Complexity - O(n^2)
#Space Complexity - O(1)

"""
QuickSort is a sorting algorithm based on 
the Divide and Conquer algorithm 
that picks an element as a pivot and partitions
the given array around the picked 
pivot by placing the pivot in its correct 
position in the sorted array.
"""

def quick_sort(arr):
    l = len(arr)
