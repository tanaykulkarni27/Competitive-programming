def read_str():
    return input()
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]

def solve(st):
    first_team_count = second_team_count = 0
    global_first = 0
    global_second = 0
    for i in st:
        if int(i) == 0:
            first_team_count+=1
            if first_team_count==7:
                return "YES"
        else:
            global_first = max(global_first,first_team_count)
            first_team_count*=0
        if int(i) == 1:
            second_team_count+=1
            if second_team_count==7:
                return "YES"
        else:
            global_second = max(global_second,second_team_count)
            second_team_count*=0
    return "NO"
st = read_str()
ans = solve(st)
print(ans)
