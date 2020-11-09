# import sys
# sys.setrecursionlimit(int(100000))
def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
# temp = 0

def pow(n,p,mod,memo):
    if (n,p) in memo: return memo.get((n,p))
    if p == 0:
        return 1
    half_pow = pow(n,p//2,mod,memo)
    half_sqr = (half_pow*half_pow)%mod
    if p%2 == 0:
        memo[(n,p)] = half_sqr
        return half_sqr
    else:
        memo[(n, p)] = (half_sqr*n)%mod
        return (half_sqr*n)%mod
def solve():
    ans = A%P
    memo = {}
    for i in range(2,N+1):
        ans = pow(ans,i,P,memo)
    return ans
T = read_int()
for _ in range(1,T+1):
    A,N,P = read_int_array()
    ans = solve()
    print('Case #{}:'.format(_),end=' ')
    print(ans)
