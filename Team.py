def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def filter(arr):
    for i in range(len(arr)):
        if 0 in arr:
            arr.remove(0)
    return arr
def solve(mat):
    count = 0
    for i in mat:
        if len(i)>=2:
            count+=1
    return count
N = read_int()
mat = []
for _ in range(1,N+1):
    temp = read_int_array()
    mat.append(filter(temp))
ans = solve(mat)
print(ans)
'''
3
1 1 0
1 1 1
1 0 0
 
'''
