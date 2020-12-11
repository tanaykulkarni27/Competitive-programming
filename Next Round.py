def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]

def solve(arr,k):
    count = 0;kth_score = arr[k-1]
    for i in arr:
        if i>=kth_score and i!=0:
            count+=1
    return count
N,K = read_int_array()
arr = read_int_array()
ans = solve(arr,K)
print(ans)
