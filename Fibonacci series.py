memo = {}
def fib(n,memo):
    if n ==1 or n==2:
        return 1
    elif memo.get(n)!=None:
        return memo[n]
    else:
        tmp = fib(n-1,memo)+fib(n-2,memo)
        memo[n] =tmp
        return tmp
print(fib(900,memo))
