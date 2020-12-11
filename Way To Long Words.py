def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def solve(st):
    if len(st)<=10:
        print(st)
        return
    else:
        print("{}{}{}".format(st[0],len(st)-2,st[-1]))
        return
N = read_int()
for _ in range(1,N+1):
    s = read_str()
    solve(s)
'''
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
'''
