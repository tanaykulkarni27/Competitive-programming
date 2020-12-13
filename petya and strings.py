def read_str():
    return input()
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
def chars():
    characters = []
    for i in range(97,123):
        characters.append(chr(i))
    return characters
def solve(s1,s2):
    for i in range(len(s1)):
        if s1[i]<s2[i]:
            return -1
        elif s1[i]>s2[i]:
            return 1
    return 0
s1 = read_str().lower()
s2 = read_str().lower()
ans = solve(s1,s2)
print(ans)
'''
if first string is greater than the second return -1

else if first string is smaller than the second return 1
else 
return 0
'''
