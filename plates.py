'''
input (sample dataset)  
sample 
T = testCase
N,P,K
new N lines for each K integers array

dataset

3
3 2 2
20 10
15 50
80 80
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10
'''

def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
memo = {}
def solve():
    memo.clear()
    dp = stack
    for i in range(len(stack)):
        for j in range(len(stack[0])-1):
            dp[i][j+1] += dp[i][j]
    res = dfs(0,P,dp)
    dp.clear()
    return res
def dfs(i,p,dp):
    if (i,p) in memo:
        return memo.get((i,p))
    if p ==0:
        return 0
    if i >=len(stack):
        return 0
    else:
        res = 0
        for j in range(K+1):
            if j == 0:
                res = max(res,dfs(i+1,p,dp))   # we are exncluding the current item and
            elif p>=j:
                res = max(res,dfs(i+1,p-j,dp)+dp[i][j-1]) #we are including the current item
        memo[(i,p)] = res
        return res
T = read_int()
for _ in range(1,T+1):
    N,K,P = read_int_array()
    stack = []
    for i in range(N):
        plates = read_int_array()
        stack.append(plates)
    dps = [[-1]*(len(stack)+5)]*(P+5)
    ans = solve()
    print('Case #{}: {}'.format(_,ans))
