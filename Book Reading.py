class case:
    def __init__(self,reader_m,pages,torned):
        self.torned = torned
        self.reader_m = reader_m
        self.pages = pages
    def solve(self):
        ans = 0
        for page in range(1,self.pages+1):
            if page not in self.torned:
                for reader in self.reader_m:
                    if page%reader == 0:
                         ans+=1
        return ans
T = int(input())
for i in range(1,T+1):
    pages,torn_pages,reader = [int(i) for i in input().split()]
    torned_page_number = [int(i) for i in input().split()]
    reader_multiples = [int(i) for i in input().split()]
    obj = case(reader_multiples,pages,torned_page_number)
    ans = obj.solve()
    print('Case #{}: {}'.format(i,ans))
# Test Input
'''
3
11 1 2
8
2 3
11 11 11
1 2 3 4 5 6 7 8 9 10 11
1 2 3 4 5 6 7 8 9 10 11
1000 6 1
4 8 15 16 23 42
1
'''
