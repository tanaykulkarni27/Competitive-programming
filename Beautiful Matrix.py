def read_str():
    return input()
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]

def solve(mat):
    if mat[2][2] == 1:
        return 0
    else:
        counter = 0
        for i in range(5):
            for j in range(5):
                if mat[i][j] == 1:
                    if i>2:
                        last = i-2
                        for k in range(last):
                            mat[i],mat[i-1] = mat[i-1],mat[i]
                            counter+=1
                    elif i<2:
                        last = 2-i
                        for k in range(last):
                            mat[i],mat[i+1] = mat[i+1],mat[i]
                            counter+=1
                    if j>2:
                        last = j-2
                        for k in range(last):
                            mat[i][j],mat[i][j-1] = mat[i][j-1],mat[i][j]
                            counter+=1
                    elif j<2:
                        last = 2-j
                        for k in range(last):
                            mat[i][j], mat[i][j + 1] = mat[i][j + 1], mat[i][j]
                            counter+=1
                    return counter


matrix = []
for _ in range(5):
    temp = read_int_array()
    matrix.append(temp)
ans = solve(matrix)
print(ans)
