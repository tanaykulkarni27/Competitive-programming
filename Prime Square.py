def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return True
    return False
def nxt(n):
    if n%2 ==0:
        for i in range(1,int(1e5)+1,2):
            if is_prime(n+i) == False and is_prime(i):
                return int(i)
    else:
        for i in range(2,int(1e5)+1,2):
            if is_prime(n+i) == False and is_prime(i):
                return int(i)
def last_nxt(n1,n2):
    for i in range(4,int(1e5)+1):
        if is_prime(n1+i) == False and is_prime(n2+i) == False and is_prime(i):
            return int(i)
    return None
def get_sum(arr,l):
    ss = 0
    for j in range(0,len(arr)-1):
        ss+=arr[j][l]
    return ss
def even_s():
    evens = []
    for i in range(4,250,2):
        evens.append(i)
    return evens
def solve(n):
    even = even_s()
    temp = even[:n - 1]
    temp.append(nxt(sum(temp)))
    mat = [temp]*int(n-1)
    mat.append([])
    for l in range(0,n-1):
        sm = even[l]*(n-1)
        mat[-1].append(nxt(sm))
    t = len(mat[0])-1
    mat[-1].append(last_nxt(mat[0][t]*(n-1),sum(mat[n-1])))
    return mat
T = read_int()
for _ in range(1, T + 1):
    N = read_int()
    ans = solve(N)
    for i in ans:
        print(*i)
