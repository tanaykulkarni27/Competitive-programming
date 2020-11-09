import sys
sys.setrecursionlimit(int(100000))
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
    if p == 1:
        return n
    if (n,p) in memo:
        return memo.get((n,p))
    else:
        ans = n*pow(n,p-1,memo)
        memo[(n,p)] = ans
        return ans
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
