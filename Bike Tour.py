class case :
    def __init__(self,H,N):
        self.N = N
        self.H = H
        self.counter = 0
    def solution(self,H,i,counter):
        if i>len(H)-2:
            return counter
        else:
            if H[i-1]<H[i] and H[i]>H[i+1]:
                counter+=1
            return self.solution(H,i+1,counter)
    def get_result(self):
        ans = self.solution(self.H,1,self.counter)
        return ans
T  = int(input())
for i in range(1,T+1):
    N  = int(input())
    H = [int(i) for i in input().split(sep=' ')]
    obj = case(H,N)
    ans = obj.get_result()
    print('Case #{}: {}'.format(i,ans))
