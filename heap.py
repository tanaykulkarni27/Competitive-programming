'''
arr_indexes = 1,2,3,4,5,6
        0    1  2  3  4  5  6 7  8
arr = [None, 13, 17, 20, 1, 5,10,15]
                                1
                              /   \
                             2     3
                           /  \   /
                          4    5  6
'''
# N is number of elements in an array
# arr is the array
# index is the position of
def heapify(arr,n,i):
    large = i
    left =  2*i+1
    right = 2*i+2
    while left<n and arr[left]>arr[large]:
        large = left
    while right<n and arr[right]>arr[large]:
        large = right
    if large!= i:
        arr[large],arr[i] = arr[i],arr[large]
        heapify(arr,n,large)

def heap(arr,n):
    # build the max heap from  the array
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    # Exporting the largest element of array 1 by 1 
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i] 
        heapify(arr,i,0) # checking after swaping tree is still statifying the conditions of max heap or not 

arr = [12, 11, 13, 5, 6, 7]
print(*arr)
heap(arr,6)
print(*arr)
