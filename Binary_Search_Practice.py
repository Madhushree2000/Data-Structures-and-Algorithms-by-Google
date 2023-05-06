"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(arr, value):
    u = len(arr)-1
    l = 0
    mid = 0
    ans = -1
    while(u >= l):
        mid = (u + l)//2
        if (arr[mid] == value):
            ans = mid
            break
        if (arr[mid]< value):
            l = mid + 1
        if (arr[mid] > value):
            u = mid - 1
    return(ans)

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))