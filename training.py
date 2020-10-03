class case:
    def __init__(self,P,S):
        self.P = P
        self.S = S
    def get_result(self):
        # self.S.sort()
        timer = 0
        for i in range(len(self.S)-2):
            if self.S[i] == max(self.S):
                self.P=self.P-1
                if self.P ==0:
                    return 0
            else:
                if self.S[i]<=self.S[len(self.S)-2]:
                    while self.S[i]<self.S[len(self.S)-2]:
                        timer += 1
                        self.S[i]+=1
        return timer
if __name__ or '__main__':
    T = int(input())  # No of test Case
    for i in range(1,T+1):
        N,P = [int(i) for i in input().split()] # P = No of Students Required for team,N = Total No of students
        S = [int(i) for i in input().split()] #list of skill rating of the students
        obj = case(P,S)
        ans = obj.get_result()
        print('Case #{}: {}'.format(i,ans))

