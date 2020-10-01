class case:
    def __init__(self,A):
        self.A = A
    def get_result(self):
        counter = 1
        lengths = []
        for i in range(1,len(self.A)-1):
          varA = self.A[i] - self.A[i-1]
          VarB = self.A[i+1] - self.A[i]
          if varA  == VarB:
            counter = 1
            for j in range(i-1,len(self.A)-1):
                if self.A[j+1]-self.A[j] == varA:
                    counter = counter+1
            if counter>1:
                lengths.append(counter)
        if len(lengths)>0:
            return max(lengths)
        else:
            return 0
Case = int(input())
N = int(input())
A = [int(i) for i in input().split()]
if N == len(A):
    ans = case(A).get_result()
    print('Case #{}: {}'.format(Case,ans))
