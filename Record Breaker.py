class case:
    def __init__(self,No,Vistors):
        self.No_of_days = No
        self.visitors = Vistors
        self.Days_counter = 0
    def max(self,a,b):
        if a>b:
            return a
        elif b>a:
            return b
        elif a == b:
            return a
    def get_solution(self):
        previous_record = 0;new_record=0
        for i in range(len(self.visitors)):
# if day is first day or vistors of day is greater than the previous record breaking day  and if day is second last day or number of visitors second_last day > no of visitors last Day
            if ( i == 0 or self.visitors[i]>previous_record )and (i+1==len(self.visitors) or self.visitors[i]>self.visitors[i+1]):
                new_record+=1                                                                                                        # count's the Number of record breaking days
            previous_record = self.max(previous_record,self.visitors[i])  # for checking new day is record breaking or not
        return new_record
T = int(input())
for i in range(1,T+1):
    No_of_Days  = int(input())
    No_of_visitors_per_day = [ int(i) for i in input().split() ]
    obj = case(No_of_Days,No_of_visitors_per_day)
    ans = obj.get_solution()
    print('Case #{}: {}'.format(i,ans))
