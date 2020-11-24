from math import sqrt
def read_int():
    return int(input())
def read_string():
    return str(input())
def read_int_array():
    return [int(i) for i in input().split()]
def read_str_array():
    return [str(i) for i in input().split()]
def chk(N): # Checking N is Perfect Square of Not
    i = int(sqrt(N))
    if N == int(i*i) :
        return True
    else:
        return False
def s(N):
    return N*N
def solve(N):
    if chk(N):return 1
    else:
        for i in range(1,int(sqrt(N))+1):
            for j in range(i,int(sqrt(N))+1):
                if (i*i+j*j == N):
                    return 2
        for i in range(1,int(sqrt(N))+1):
            for j in range(i,int(sqrt(N))+1):
                for k in range(j,int(sqrt(N))+1):
                    if (s(i)+s(j)+s(k) == N):
                        return 3
        return 4
T = int(input())
for _ in range(1,T+1):
    N = read_int()
    ans = solve(N)
    print('Case #{}: {}'.format(_,ans))
