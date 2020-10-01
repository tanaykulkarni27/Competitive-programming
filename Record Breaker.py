class case:
    def __init__(self,N,Ni):
        self.N = N
        self.Ni = Ni
    def get_result(self):
        counter = 0;k = False;i=0;
        for i in range(1,len(self.Ni)):
            if  self.Ni[i]>self.Ni[i-1]:
                chk = 0
                for j in range(i):
                    if self.Ni[i]>self.Ni[j]:
                        chk  =  chk+1
                    else:
                        break;
                if chk == i:
                    counter = counter+1

        return counter
Case = int(input())
N  = int(input())
Ni = [ int(i) for i in input().split(sep=' ') ]
obj = case(N,Ni)
ans = obj.get_result()
print('Case #{}: {}'.format(Case,ans))
