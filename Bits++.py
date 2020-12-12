def read_str():
    return input()
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]

def solve(arr):
    x = 0
    for i in arr:
        if i == "X++" or i == "++X":
            x+=1
        else:
            x-=1
    return x
arr = []
n = read_int()
for _ in range(n):
    s = read_str()
    arr.append(s)
ans = solve(arr)
print(ans)
