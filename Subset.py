import sys
sys.setrecursionlimit(100000000)
def read_int():
    return int(input())
def read_string():
    return str(input())
def read_int_array():
    return [int(i) for i in input().split()]
def read_str_array():
    return [str(i) for i in input().split()]
class ss:
    def __init__(self):
        self.ans =  0
    def fi(self,arr,index,subset): # prints the subsets in which ai is the minimum value
        if 0<=index>=len(arr):
            self.ans+= int(max(subset)-min(subset))
        else:
            subset.append(arr[index])
            self.fi(arr,index+1,subset)
            subset.pop(-1)
            self.fi(arr,index+1,subset)
    def main(self,arr):
        for i in range(len(arr)):
            subset = []
            subset.append(arr[i])
            self.fi(arr,i+1,subset)
T = read_int()
for _ in range(1,T+1):
    N = read_int()
    arr = read_int_array()
    ob = ss()
    ob.main(arr)
    print('Case #{}:'.format(_), end=' ')
    print(ob.ans)
