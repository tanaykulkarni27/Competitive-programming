class case:
    def __init__(self,X,A):
        self.A = A
        self.X = X
    def get_result(self):
        order = []
        for j in range(len(self.A)):
            for i in range(len(self.A)):
                if self.A[i]!=0:
                    if self.A[i]<=self.X:
                        order.append(i+1)
                        self.A[i] = 0
                    else:
                        self.A[i] = self.A[i]-self.X
            if len(order) == len(self.A):
                return order
Case = int(input())
N,X = [int(j) for j in input().split()]
A = [int(i) for i in input().split()]
obj = case(X,A)
ans = obj.get_result()
final = ''
for i in ans:
    final += str(i)+' '
print('Case #{}: {}'.format(Case,final))
