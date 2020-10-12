import sys
sys.setrecursionlimit(100000000)
class case:
    def __init__(self,N,Max,Money):
        self. No_of_Presons_in_Queue = N
        self.Maximum_amount_to_withdraw = Max
        self.Money_to_Withdraw = Money
        self.Queue = []
    def recursion(self,Max,Money_to_withdraw,i,Queue):
        if len(Queue)== len(Money_to_Withdraw):
            return Queue
        if Money_to_Withdraw[i] <= Max and Money_to_Withdraw[i]!=0:
            Money_to_Withdraw[i] = 0
            Queue.append(i+1)
            if i+1 <= len(Money_to_Withdraw)-1:
                return self.recursion(Max,Money_to_Withdraw,i+1,Queue)
            else:
                return self.recursion(Max,Money_to_Withdraw,0,Queue)
        elif  Money_to_Withdraw[i] > Max and Money_to_Withdraw[i]!=0:
            Money_to_Withdraw[i] -=Max
            if i + 1 < len(Money_to_Withdraw):
                return self.recursion(Max, Money_to_Withdraw, i + 1, Queue)
            else:
                return self.recursion(Max, Money_to_Withdraw, 0, Queue)
        else:
            if i+1 <= len(Money_to_Withdraw)-1:
                return self.recursion(Max,Money_to_Withdraw,i+1,Queue)
            else:
                return self.recursion(Max,Money_to_Withdraw,0,Queue)
    def get_result(self):
        ans = self.recursion(self.Maximum_amount_to_withdraw,self.Money_to_Withdraw,0,self.Queue)
        t=''
        for i in ans:
            t+=str(i)+' '
        return t
T = int(input())
for i in range(1,T+1):
    No_of_Presons_in_Queue,Maximum_amount_to_withdraw = [int(j) for j in input().split()]
    Money_to_Withdraw = [int(j) for j in input().split()]
    obj = case(No_of_Presons_in_Queue,Maximum_amount_to_withdraw,Money_to_Withdraw)
    ans = obj.get_result()
    print('Case #{}: {}'.format(i,ans))
