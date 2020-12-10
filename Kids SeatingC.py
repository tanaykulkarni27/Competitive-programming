import math
def read_str():
    return str(input())


def read_int():
    return int(input())


def read_str_array():
    return [str(i) for i in input().split()]


def read_int_array():
    return [int(i) for i in input().split()]
def chk_chair(chair,arr):
    for i in range(0,len(arr)):
        if chair%arr[i] ==0 or arr[i]%chair == 0 or math.gcd(arr[i],chair)==1:
            return False
    return True
def get_num(arr,n):
    chair = 4*n-1
    while(chair>=1):
        if chair not in arr and chk_chair(chair,arr) :
            return chair
        chair-=1
def solve(arr,N):
    for i in range(1,N):
        arr.append(get_num(arr,N))
    return arr

T = read_int()
for _ in range(1, T + 1):
    N = read_int()
    ans = solve([4*N],N)
    print(*ans)
