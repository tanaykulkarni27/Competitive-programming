class case:
    def __init__(self,M):
        self.N = N
        self.cakes_need_to_eat = 0
        self.i =1

    def square_root(self,N, i):
        if N == 1:
            return 1
        if i * i == N:
            return i
        elif i * i > N:
            return i - 1
        else:
            return self.square_root(N, i + 1)
    def recursive(self,N,cakes_eaten):
        if N <= 0:
            return cakes_eaten
        a = self.square_root(N,1)
        cakes_eaten+=1
        return self.recursive(N-a*a,cakes_eaten)
    def get_result(self):
        ans = self.recursive(self.N,self.cakes_need_to_eat)
        return ans
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    obj = case(N)
    ans = obj.get_result()
    print('Case #{}: {}'.format(test_case,ans))
