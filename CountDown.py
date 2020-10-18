class case:
    def __init__(self,A,K):
        self.K = K
        self.A = A
        self.chk = False
        self.decreasing_counter = 0
    def solve(self):
        count_downs = 0;i=0
        while i < len(self.A):
            if self.K-self.decreasing_counter == self.A[i] and i == len(self.A)-1 and self.chk:
                count_downs+=1
            if self.A[i] == self.K-self.decreasing_counter:
                self.decreasing_counter+=1
                self.chk = True
            elif self.A[i] != self.K-self.decreasing_counter and self.K and self.decreasing_counter>1:
                count_downs+=1
                self.decreasing_counter*=0
                self.chk = False
                if self.A[i] == self.K:
                    i-=1
            i+=1
        return count_downs
T = int(input())
for i in range(1,T+1):
    N,K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    obj =  case(A,K)
    ans = obj.solve()
    print('Case #{}: {}'.format(i,ans))
