class case:
    def __init__(self,bought,expiry_days,max):
        self.max = max
        self.bought = bought
        self.expiry_days = expiry_days

    def get_result(self):
        consumed = 0;consumed_today = 0;day = 0;
        for i in range(self.bought):
            if consumed_today == self.max:
                day+=1
                consumed_today = 0
            if self.expiry_days[i] > day:
                consumed_today+=1
                consumed+=1
        return consumed
T = int(input())
for i in range(1, T + 1):
    N, K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    obj = case(N,A,K)
    ans = obj.get_result()
    print('Case #{}: {}'.format(i,ans))
