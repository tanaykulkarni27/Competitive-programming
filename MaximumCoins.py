class case:
    def __init__(self,Matrix):
        self.Matrix = Matrix
        self.answer = 0
    def max(self,a,b):
        if a>b:
            return a
        elif b>a:
            return b
        else:
            return a
    def get_diagonal_sum(self,coins, row, column):
        calculated = 0;
        coin_row = row;
        coin_column = column
        while (coin_row < len(coins) and coin_column < len(coins[0])):
            calculated += coins[coin_row][coin_column]
            coin_row += 1
            coin_column += 1
        return calculated
    def solve(self):
        answer = 0;
        for i in range(len(self.Matrix)):
            answer = self.max(answer,self.get_diagonal_sum(self.Matrix,0,i))
        for i in range(len(self.Matrix)):
            answer = self.max(answer,self.get_diagonal_sum(self.Matrix,i,0))
        return answer
T = int(input())
for i in range(1,T+1):
    N = int(input())
    matrix = []
    for column in range(N):
         row = [int(i) for i in input().split()]
         matrix.append(row)
    obj = case(matrix)
    ans = obj.solve()
    print('Case #{}: {}'.format(i,ans))
