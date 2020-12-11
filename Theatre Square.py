def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def get_tiles(N,A):
    count = 0
    temp = N//A
    if N%A != 0:
        count+=int(temp+1)
    else:
        count+=int(temp)
    return count
def solve(N,M,A):
    # get_tiles(N,A)*get_tiles(M,A)
    return get_tiles(N,A)*get_tiles(M,A)
N,M,A = read_int_array()
ans = solve(N,M,A)
print(ans)
 
'''
6 6 4
'''
