#Divide and Conquer

#Time Complexity - O(nlogn)
#Space Complexity - O(n)

"""
Merge sort is defined as a sorting algorithm 
that works by dividing an array into 
smaller subarrays, sorting each subarray, 
and then merging the sorted subarrays 
back together to form the final sorted array.
"""

def merge_sort(arr):
    if (len(arr) > 1): 
        mid = len(arr)//2

        L_arr = arr[:mid]
        R_arr = arr[mid:]

        merge_sort(L_arr)
        merge_sort(R_arr)

        i = j = k = 0

        while i < len(L_arr) and j < len(R_arr):
            if L_arr[i] <= R_arr[j]:
                arr[k] = L_arr[i]
                i+=1
            else:
                arr[k] = R_arr[j]
                j+=1
            k+=1

        while i < len(L_arr):
            arr[k] = L_arr[i]
            i+=1
            k+=1

        while j < len(R_arr):
            arr[k] = R_arr[j]
            j+=1
            k+=1
        
    return arr


test = [21, 4, 1, 3, 9, 20, 25]
print(merge_sort(test))