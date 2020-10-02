class case:
    def __init__(self,A,B,N):
        self.A = A
        self.B = B
        self.N = N
    def get_result(self):
        random = int(((self.B-self.A)-2)/2)
        for i in range(self.N):
            guess = int(input())
            result = self.chk(guess,random)
            if result:
                format = 'Case #{}: {}'.format(Case, 'CORRECT')
                print(format)
                return 0
            else:
                if guess>random:
                    format = 'Case #{}: {}'.format(Case, 'TOO_BIG')
                    print(format)
                else:
                    format = 'Case #{}: {}'.format(Case, 'TOO_SMALL')
                    print(format)
        format = 'Case #{}: {}'.format(Case, 'WRONG_ANSWER')
        print(format)
    def chk(self,guess,random):
        for i in range(self.A,self.B):
                if guess == random :
                    return True

Case = int(input())
A,B = [int(i) for i in input().split()]
N = int(input())
obj = case(A,B,N)
obj.get_result()
