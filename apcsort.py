def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def solve():
    alex = [];bob=[];index_a = 0
    index_b=0
    for price in S:
        if price%2==0:
            bob.append(price)
        elif price%2 !=0:
            alex.append(price)
    alex = sorted(alex)
    bob.sort()
    bob.reverse()
    # print(alex)
    # print(bob)
    for j in range(len(S)):
        if S[j] %2 == 0:
            S[j] = bob[index_b]
            index_b+=1
        if S[j] %2 != 0:
            S[j] = alex[index_a]
            index_a+=1
    return S
T = read_int()
for _ in range(1,T+1):
    N = read_int()
    S = read_int_array()
    ans = solve()
    print('Case #{}:'.format(_),end=' ')
    print(*ans)
