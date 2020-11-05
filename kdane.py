'''

kadane's Algorithm

maximum subarray

test set

1
-2 3 2 -1

'''
def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def kadane(arr):
    max_current = max_global = arr[0]
    for i in range(1,len(arr)):
        max_current = max(arr[i],max_current+arr[i])
        max_global = max(max_global,max_current)
    return max_global
T = read_int()
for _ in range(1,T+1):
    array = read_int_array()
    print(kadane(array))
