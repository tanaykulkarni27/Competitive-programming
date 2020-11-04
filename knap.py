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
'''

1
3 50
60 100 120
10 20 30

answer = 220

'''
def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def KS_bottom_up(W,val,wt,index):
    K = [[0 for x in range(W + 1)] for y in range(n + 1)]
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0 :
                K[i][j] = 0
            elif wt[i-1]<=j:
                K[i][j] = max(val[i-1]+K[i-1][j-wt[i-1]],K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    return K[n][W]
def KS_recursion(W,val,wt,index):
    if W == 0 or index>=len(wt):return 0
    elif wt[index]>W:
        return KS_recursion(W,val,wt,index+1)
    else:
        res = max(val[index]+KS_recursion(W-wt[index],val,wt,index+1),KS_recursion(W,val,wt,index+1))
        return res
T= read_int()
for _ in range(1,T+1):
    n,K = read_int_array()
    values = read_int_array()
    weights = read_int_array()
    ans = KS_recursion(K,values,weights,0)
    print('Case #{}: {}'.format(_,ans))
