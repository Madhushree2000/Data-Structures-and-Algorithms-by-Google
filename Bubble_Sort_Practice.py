#Best Case - O(n)
#Average Case - O(n^2)
#Worst Case - O(n^2)

#Space Complexity - O(1)

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n,1):
        for j in range(0, n-1-i,1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

test1 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14] 
test2 =  [120, 140, 32, 56, 34, 72, 200, 45, 76, 23,9]
print(bubble_sort(test1))
print(bubble_sort(test2))