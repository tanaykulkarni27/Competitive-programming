class case:
    def __init__(self,reader_m,pages,torned):
        self.torned = torned
        self.reader_m = reader_m
        self.pages = pages
    def solve(self):
        ans = 0;X=1
        for reader in self.reader_m:
            X=1
            while reader*X <= self.pages :
                if reader*X not in self.torned:
                    ans+=1
                X+=1
        return ans
T = int(input())
for i in range(1,T+1):
    pages,torn_pages,reader = [int(i) for i in input().split()]
    torned_page_number = [int(i) for i in input().split()]
    reader_multiples = [int(i) for i in input().split()]
    obj = case(reader_multiples,pages,torned_page_number)
    ans = obj.solve()
    print('Case #{}: {}'.format(i,ans))
