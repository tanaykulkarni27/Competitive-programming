def read_int():
    return int(input())
def read_string():
    return str(input())
def read_int_array():
    return [int(i) for i in input().split()]
def read_str_array():
    return [str(i) for i in input().split()]
def is_beautiful(N):
    for i in str(N):
        if int(i)%2 !=0:
            return False
    return N
def previous(st):
    i  = st
    while i>=0 and is_beautiful(i) == False :
        i-=1
    if i>=0:
        return st-i
    else:
        return st+1000000000000000000
def next(st):
    i = st
    while is_beautiful(i) == False:
        i += 1
    return i-st
def solve(N):
    temp = N
    return min(next(temp),previous(temp))
T = read_int()
for _ in range(1,T+1):
    N = read_int()
    ans = solve (N)
    print('Case #{}: {}'.format(_,ans))
