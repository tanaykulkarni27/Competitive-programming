class MyStack:
    def __init__(self):
        self.A = []
        self.p = 0
        self.i = 0
    def push(self,N):
        self.A.append(N)
        self.p+=1
        self.i=self.p
    def pop(self,k=None):
        if k!=None:
            self.A.pop(k)
            self.p-=1
            self.i=self.p
        else:
            if self.p -1 >0:
                self.A.pop(self.p-1)
                self.p-=1
                self.i = self.p
            else:
                self.A.pop(0)
    def peek(self,k=None):
        if k !=None:
            print(self.A[k])
        else:
            if self.i-1 >0:
                print(self.A[self.i-1])
                self.i -= 1
            else:
                print(self.A[0])

        return ''
    def get_length(self):
        return len(self.A)
