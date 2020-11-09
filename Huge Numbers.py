import sys
sys.setrecursionlimit(int(1000000))
def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
# temp = 0

def pow(n,p,memo = {}):
    if p == 0:
        return 1
    half_pow = pow(n,p//2)
    half_sqr = (half_pow*half_pow)
    if p%2 == 0:
        return half_sqr
    else:
        return half_sqr*n
def solve():
    ans = A%P
    for i in range(2,N+1):
        ans = pow(ans,i)%P
    return ans
T = read_int()
for _ in range(1,T+1):
    A,N,P = read_int_array()
    ans = solve()
    print('Case #{}:'.format(_),end=' ')
    print(ans)
