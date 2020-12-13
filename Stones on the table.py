'''
test input
3
RRG

5
RRRRR

4
BRBG

ans of test input = 1 4 0
'''
def read_str():
    return input()
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]

def solve(st):
    count = 0
    for i in range(len(st)):
        if 0<=i-1<len(st) and  st[i]==st[i-1]:
            count+=1
    return count
N = read_int()
st = read_str()
ans = solve(st)
print(ans)
