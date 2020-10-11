class case:
    def __init__(self,A,N,P):
        self.A = A
        self.N = N
        self.P = P
        self.tmp = 1
        self.memo = {}
    def find_ans(self,A,N):
        if N > self.N:
            return self.tmp%self.P
        self.tmp = self.pow(A,N,self.memo)
        return self.find_ans(self.tmp,N+1)
    def pow(self,A,n,memo):
        if n == 0:
            return 1
        elif memo.get(n)!=None:
            return memo.get(n)
        else:
            a = A* self.pow(A,n-1,memo)
            memo[n]=a
            return a
    def get_result(self):
        final = self.find_ans(self.A,1)
        return final
T = int(input())
for i in range(1,T+1):
    A,N,P = [int(j) for j in input().split()]
    obj = case(A,N,P)
    ans = obj.get_result()
    print('Case #{}: {}'.format(i,ans))
