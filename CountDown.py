'''
1
3 3
3 2 2 1 3 2 1
'''

def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def solve():
    i = 0;counter = 0; decreasing_counter = 0
    while i < len(A):
        j = i;decreasing_counter = 0
        if A[i] == S:
            while j<len(A) and A[j] == S-decreasing_counter >=1:
                j+=1
                decreasing_counter+=1
        if decreasing_counter>1 and S-decreasing_counter == 0 :
            counter+=1
        i = max(i+1,j)
    return counter
T = read_int()
for  _ in range(1,T+1):
    N,S = read_int_array()
    A =  read_int_array()
    ans = solve()
    print('Case #{}:'.format(_),end=' ')
    print(ans)
