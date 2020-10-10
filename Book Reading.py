class case :
    def __init__(self,No_of_pages,list_of_torn_pages,list_of_multiples):
        self.No_of_pages = No_of_pages
        self.list_of_torn_pages = sorted(list_of_torn_pages)
        self.list_of_multiples = list_of_multiples
        self.count = 0
    def get_result(self):
        for j in list_of_multiples:
            for i in range(1,self.No_of_pages+1):
                if i%j==0:
                    length = len(self.list_of_torn_pages)-1
                    result = self.search(self.list_of_torn_pages,0,length,i)
                    if result:
                        self.count+=1
        return self.count
    def search(self, array,l,r,  target):
        mid = (l+r)//2
        if l>r:
            return True
        if array[mid] ==target or array[0]==target or array[r]==target:
            return False
        elif array[mid]>target:
            return self.search(array,l,mid-1,target)
        elif array[mid]<target:
            return self.search(array,mid+1,r,target)
T = int(input())
for i in range(1,T+1):
    No_of_pages,No_of_torn_pages,No_of_reader = [int(i) for i in input().split()]
    list_of_torn_pages = [int(i) for i in input().split()]
    list_of_multiples = [int(i) for i in input().split()]
    obj = case(No_of_pages,list_of_torn_pages,list_of_multiples)
    ans = obj.get_result()
    print('Case #{}: {}'.format(i,ans))
