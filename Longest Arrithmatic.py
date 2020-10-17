class case:
    def __init__(self,A):
        self.integers = A
        self.Max_Length = 0
        self.Old_Max_Length = 0
    def get_solution(self):
        for i in range(len(self.integers)-1):
            j = i;temp = 1
            common_difference = self.integers[i+1]-self.integers[i]
            while j<len(self.integers)-1:
                if self.integers[j+1]-self.integers[j]==common_difference:
                    temp+=1
                else:
                    break
                j+=1
            self.Max_Length = temp
            if self.Max_Length > self.Old_Max_Length:
                self.Old_Max_Length=self.Max_Length
        return self.Old_Max_Length
T = int(input())
for i in range(1, T + 1):
    N = int(input())
    integers = [int(i) for i in input().split()]
    obj = case(integers)
    ans = obj.get_solution()
    print('Case #{}: {}'.format(i,ans))
