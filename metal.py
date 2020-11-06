def read_str():
    return str(input())


def read_int():
    return int(input())


def read_str_array():
    return [str(i) for i in input().split()]


def read_int_array():
    return [int(i) for i in input().split()]


def sort_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][0] > matrix[j][0]:
                temp = matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = temp
    return matrix


def solve():
    robot = 0;
    time = 0
    sort_matrix(intervals)
    # print(intervals)
    for s, e in intervals:
        if s > time:
            time = s
        if e > time:
            while time < e:
                # print(time)
                time += Time_of_harvesting
                robot += 1

    return robot


T = read_int()
for _ in range(1, T + 1):
    No_of_intervals, Time_of_harvesting = read_int_array()
    intervals = list()
    for i in range(No_of_intervals):
        interval = read_int_array()
        intervals.append(sorted(interval))
    ans = solve()
    print('Case #{}: {}'.format(_, ans))

'''
3
3 5
1 5
10 11
8 9
3 2
1 2
3 5
13 14    
3 2
1 4
4 5
5 4

    #dp = [];
    # for j in intervals:
    #     dp+=j
    # dp.sort()
    # time = dp[0]

'''
