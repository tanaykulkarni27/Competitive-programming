'''
Data Set 'Example Input'

1
50
10 20 30
60 100 120

Answer:
Case #1: 220

assume that dp[n][len(w)] is the maximum number of items


'''
def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def dp_using_bottom_up(index):   # this is bottom up approach Time it takes n * w(   capacity of knapsack    )
    dp= [[0]*len(weights)]*len(weights)
    for i in range(len(weights)):
        for j in range(len(weights)):
            if i ==0 or j==0:
                dp[i][j] = 0
            elif weights[i]<=capacity:
                dp[i][j] =  max(dp[i-1][j],prices[i]+dp[i-1][j-weights[i]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[i][j]
def dp_using_recursion(c,w,v,index,memo):   # this is recursive approach Time it takes n^2
   if index == 0 or c == 0:
       return 0
   if w[index]>c:
       return dp_r(c,w,v,index-1)
   else:
       tmp = v[index] + dp_r(c - w[index], w, v, index - 1,memo)
       tmpb = dp_r(c,w,v,index-1,memo)
       a = max(tmp, tmpb)
       memo[len(w,),c] = a
       return a
def solve():
    result = dp_r(capacity,weights,prices,len(weights)-1,{})
    return result
T = int(input())
for _ in range(1,T+1):
    capacity = read_int()
    weights = read_int_array()
    prices = read_int_array()
    ans = solve()
    print('Case #{}: {}'.format(_,ans))
