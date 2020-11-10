from math import sqrt
import sys
sys.setrecursionlimit(int(1e5))
def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def chk_sqr(num):
    if num<0:
        return False
    temp = int(sqrt(num))
    if temp*temp == num:
        return True
    else:
        return False
def solve():
    counter = 0
    for i in range(len(arr)):
        temp = arr[i]
        if chk_sqr(temp):
            counter+=1
        for j in range(i+1,len(arr)):
            temp+=arr[j]
            if chk_sqr(temp):
                counter+=1
    return counter
T = read_int()
for  _ in range(1,T+1):
    N = read_int()
    arr = read_int_array()
    ans = solve()
    print('Case #{}: {}'.format(_,ans))
