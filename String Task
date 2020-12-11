def read_str():
    return input()
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
 
def solve(st):
    vowels = ["A", "O", "Y", "E", "U", "I","a", "o", "y", "e", "u", "i"]
    consonant = ''
    for i in st:
        if i in vowels:
            pass
        else:
            consonant+=i.lower()
    ans = ''
    for j in consonant:
        ans+='.'+j
    return ans
st = read_str()
print(solve(st))
