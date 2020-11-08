def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def solve():
    map = {};arr = sorted(array)
    for i in range(1,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if 1<=i<j<k<=N and arr[i]*arr[j] == arr[k] and (i,j,k) not in map:
                    map[(i,j,k)] = 'visited'
                elif 1<=i<j<k<=N and arr[i]*arr[k] == arr[j] and (i,k,j) not in map:
                    map[(i,k,j)] = 'visited'
                elif 1<=i<j<k<=N and arr[k]*arr[j] == arr[i] and (j,k,i) not in map:
                    map[(j,k,i)] = 'visited'
    return len(map)
T = read_int()
for _ in range(1,T+1):
    N = read_int()
    array = [-1]+read_int_array()
    ans = solve()
    print('Case #{}: {}'.format(_,ans))
