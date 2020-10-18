class case:
    def __init__(self,A,K):
        self.K = K
        self.A = A
        self.chk = False
    def solve(self):
        i=0;count = 0;ans = 0
        while i <len(self.A):
            if self.A[i] == self.K:
                count = 1
                # decreasing counter < K and index+1 < len(Array)  
                while (count<self.K and i+1<len(self.A) and self.A[i+1] == self.K-count):
                    i+=1
                    count+=1
                if count == self.K :
                    ans+=1
            i+=1
        return ans
T = int(input())
for i in range(1,T+1):
    N,K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    obj =  case(A,K)
    ans = obj.solve()
    print('Case #{}: {}'.format(i,ans))
