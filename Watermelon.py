def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def chk(N):
    for i in range(2,N):
        if i%2==0 and (N-i)%2 == 0:
            print("YES")
            return
    print("NO")
    return
N = read_int()
chk(N)
'''
100
'''
