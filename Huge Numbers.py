class case:
    def __init__(self,A,N,P):
        self.A = A
        self.N = N
        self.P = P
        self.tmp = 1
    def find_ans(self,A,N):
        if N > self.N:
            return self.tmp%self.P
        self.tmp = pow(A,N)
        return self.find_ans(self.tmp,N+1)

    def pow (self,A,n):
        if n == 0:
            return 1
        else:
            a = A* pow(A,n-1)
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
