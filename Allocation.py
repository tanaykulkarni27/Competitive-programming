class case:
    def __init__(self,A,B):
        A.sort()
        self.A = A
        self.B = B
    def get_result(self):
        y = 0
        for i in range(len(self.A)):
            if self.A[i]<=self.B:
                y = y+1
                self.B = self.B-self.A[i]
        return y
T = int(input())
for i in range(1,T+1):
    N,B = [int(j) for j in input().split()]
    A = [int(j) for j in input().split()]
    ans = case(A,B).get_result()
    print('Case #{}: {}'.format(i,ans))
