import sys
sys.setrecursionlimit(1000000)
class case:
    def __init__(self,direction,rows,colums,StartR,StartC):
        self.startX = StartR
        self.startY = StartC
        self.Rows = rows
        self.Columns = colums
        self.directions = direction
        self.Robot = [self.startX,self.startY]
    def direct_robot(self,letter,memo):
        if letter == 'N':
            self.Robot[0]-=1
            key = str(self.Robot[0])+':'+str(self.Robot[1])
            if memo.get(key) != None:
                    self.direct_robot(letter,memo)
            else:
                memo[key] = 'Visited'
        if letter == 'E':
            self.Robot[1]+=1
            key = str(self.Robot[0]) + ':' + str(self.Robot[1])
            if memo.get(key) != None:
                    self.direct_robot(letter,memo)
            else:
                memo[key] = 'Visited'
        if letter == 'W':
            self.Robot[1]-=1
            key = str(self.Robot[0]) + ':' + str(self.Robot[1])
            if memo.get(key) != None:
                    self.direct_robot(letter,memo)
            else:
                memo[key] = 'Visited'
        if letter == 'S':
            self.Robot[0]+=1
            key = str(self.Robot[0]) + ':' + str(self.Robot[1])
            if memo.get(key) != None:
                    self.direct_robot(letter,memo)
            else:
                memo[key] = 'Visited'
    def solve(self):
        memo = {}
        key = str(self.Robot[0]) + ':' + str(self.Robot[1])
        memo[key] = 'Visited'
        for i in self.directions:
            self.direct_robot(i,memo)
        return self.Robot
T = int(input())
for _ in range(1,T+1):
    N,R,C,Sr,Sc = [int(i) for i in input().split()]
    Directions = str(input())
    obj = case(Directions,R,C,Sr,Sc)
    ans = obj.solve()
    print('Case #{}:'.format(_),end=' ')
    print(*ans)
