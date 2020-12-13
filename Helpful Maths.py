def read_str():
    return input()
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]

def solve(st):
    arr = []
    for i in st:
        if i!="+":
            arr.append(i)
    arr.sort()
    ans = ""
    for i in arr:
       ans+=i+"+"
    return ans
st = read_str()
ans = solve(st)
print(ans[:len(ans)-1])
