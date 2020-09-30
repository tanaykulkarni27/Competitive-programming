class caseA:
    def __init__(self,A,K):
        self.A = A
        self.K = int(K)
    def get_range(self):
        sequence = []
        i = self.K
        while i>=1:
            sequence.append(i)
            i=i-1
        return sequence
    def get_result(self):
        sequence = self.get_range()
        counter=0;k=False
        for i in range(len(self.A)):   # checking for sequence in the Array
            if int(self.A[i]) == int(sequence[0]):
                for j in range(len(sequence)):
                    if int(self.A[i+j]) == int(sequence[j]):
                        k=True
                    else:
                        k=False
                if k:
                    counter = counter+1
        return counter
Case = int(input())
N,K  = input().split(sep=' ')
A = input().split(sep=' ')
obj = caseA(A,K)
ans = obj.get_result()
print('Case #{}: {}'.format(Case,ans))
