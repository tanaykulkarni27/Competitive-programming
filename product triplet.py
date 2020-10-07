class case:
    def __init__(self,N,A):
        A.sort()
        self.N = N
        self.A = A
    def get_result(self):
        triplet_count = 0;
        temp_zA =-5
        for x in range(0,len(self.A)-2):
            for y in range(x+1,len(self.A)-1):
                for z in range(y+1,len(self.A)):
                    if self.A[x]<=self.A[y]<=self.A[z]:
                        if self.A[x] == self.A[y] == 1 == self.A[z]:
                            if x > temp_zA and y >= temp_zA + 1:
                                if self.A[z] == self.A[x] * self.A[y]:
                                    triplet_count += 1
                                    temp_zA = z
                                    break
                        elif x <len(self.A)-2:
                            if self.A[x]<= self.A[y]<=self.A[z]:
                                if self.A[z]== self.A[x]*self.A[y]:
                                        triplet_count+=1
                                        break;
        return triplet_count
T = int(input())
for i in range(1,T+1):
    N = int(input())
    A = [int(i) for i in input().split()]
    obj = case(N,A)
    ans = obj.get_result()
    print('Case #{}: {}'.format(i,ans))
