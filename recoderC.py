def read_int():
    return int(input())
def read_str():
    return str(input())
def read_int_array():
    return [int(i) for i in input().split()]
def read_str_array():
    return [str(i) for i in input().split()]
def cal_sum(arr,i):
    sum = 0
    for j in range(i,len(arr)):
        sum+=arr[j]/(j)
    # print(sum)
    return sum
def solve(arr,M):
    global_sum = 0
    for i in range(1,len(arr)):
        global_sum += cal_sum(arr,i)
    if round(global_sum) == M:
        return "YES"
    else:
        return "NO"
T  = read_int()
for _ in range(1,T+1):
    N,M = read_int_array()
    arr = [None]+read_int_array()
    ans = solve(arr,M)
    print(ans)
