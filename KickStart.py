class case:
    def __init__(self,S):
        self.S = S
    def solve(self):
        start_string = 'KICK'; end_string = 'START';i=0;ans = 0;scnt = 0
        while i < (len(self.S)):
            if self.S[i] == start_string[0]:
                if i+4<=len(self.S):
                    if self.S[i:i+4] == 'KICK':
                        scnt+=1
            elif self.S[i] == end_string[0]:
                if i+5<=len(self.S):
                    if self.S[i:i+5] == 'START':
                        ans+=scnt
            i+=1

        return ans
T = int(input())
for i in range(1, T + 1):
    S = str(input())
    obj = case(S)
    ans = obj.solve()
    print('Case #{}: {}'.format(i,ans))
