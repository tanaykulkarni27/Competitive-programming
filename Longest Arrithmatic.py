class case:
    def __init__(self,A):
        self.integers = A
        self.Max_Length = 0
        self.Old_Max_Length = 0
    def get_solution(self):
        i=0
        while i< len(self.integers)-1:
            j = i
            common_difference = self.integers[i+1]-self.integers[i]
            while ((j<len(self.integers)-1) and (self.integers[j+1]-self.integers[j]==common_difference)):
                j+=1
            self.Old_Max_Length = max(self.Old_Max_Length,j-i+1)
            i=max(i+1,j)
        return self.Old_Max_Length
T = int(input())
for i in range(1, T + 1):
    N = int(input())
    integers = [int(i) for i in input().split()]
    obj = case(integers)
    ans = obj.get_solution()
    print('Case #{}: {}'.format(i,ans))
