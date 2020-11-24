'''
N = Total Number of levels
K = curent level
S = lvl on which i can get sword

'''
def read_int():
    return int(input())
def read_string():
    return str(input())
def read_int_array():
    return [int(i) for i in input().split()]
def read_str_array():
    return [str(i) for i in input().split()]
def exiting_game(N,S,K):
    restart = 1
    time_to_reach_current_lvl = K-1
    time_to_complete_all_lvls = N
    return (time_to_reach_current_lvl+restart+time_to_complete_all_lvls)
def going_back(N,S,K):
    time_to_reach_current_lvl = K - 1
    time_to_go_back = K-S
    time_to_complete_remaining = N+1-(S)
    return (time_to_reach_current_lvl+time_to_go_back+time_to_complete_remaining)
def solve(N,K,S):
    exiting = exiting_game(N, S, K)
    back =  going_back(N,S,K)
    return min(exiting,back)
T = int(input())
for _ in range(1,T+1):
    N,K,S = read_int_array()
    ans = solve(N,K,S)
    print('Case #{}: {}'.format(_,ans))
