class case:
    def __init__(self,D,X):
        self.X = X
        self.D = D
    def get_result(self):
        list_of_days_to_catch_the_bus=list()
        i = len(self.X)-1;k=self.D
        while i>=0:
            tmp = self.D % self.X[i]
            if  tmp ==0:
                list_of_days_to_catch_the_bus.append(self.D)
            else:
                self.D =  self.D-tmp
                list_of_days_to_catch_the_bus.append(self.D)

            i=i-1
        list_of_days_to_catch_the_bus.reverse()
        return list_of_days_to_catch_the_bus[0]
T = int(input())
for i in range(1,T+1):
    N, D = [int(i) for i in input().split()]
    X = [int(i) for i in input().split()]
    obj = case(D, X)
    ans = obj.get_result()
    print('Case #{}: {}'.format(T, ans))
