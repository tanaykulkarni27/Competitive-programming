def get_subsets(set):
    subs = []
    N = len(set)
    for i in range((1<<N)):
        subset = []
        for j in range(N):
            if 1<<j & i:
                subset.append(set[j])
        subs.append(subset)
    return subs
set = input('Enter Elements of set : ').split(sep=' ')
subset = get_subsets(set)
print(subset)
