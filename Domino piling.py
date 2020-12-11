def read_str():
    return input()
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]

def solve(st):
    pass
m,n = read_int_array()
ans = (m*n)//2
print(ans)
