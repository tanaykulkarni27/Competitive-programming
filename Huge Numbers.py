class case:
    def __init__(self,A,N,P):
        self.A = A
        self.N = N
        self.P = P


    def factorial(self,i):
        a = 1
        if i == 0:
            return a
        return i * self.factorial(i - 1)
    def get_result(self):
        ans = 1;temp=self.find_raise_to(self.A,2)
        for i in range(1,int((self.factorial(int(self.N))/2)+1)):
            ans = (ans *temp)%self.P
        return ans
    def find_raise_to(self,i, k):
        a = 1
        if k == 0:
            return a
        return i * (self.find_raise_to(i, k - 1))
T = int(input())
for i in range(1,T+1):
    A,N,P = [int(j) for j in input().split()]
    obj = case(A,N,P)
    ans = obj.get_result()
    print('Case #{}: {}'.format(i,ans))
