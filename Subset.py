def add(subset,set):
    complete = []
    if len(subset) == len(set):
        return complete
    else:
        complete.append(subset)
        return complete
def get_subsets(set):
    N = len(set)
    for i in range((1<<N)):
        subset = []
        for j in range(N):
            if 1<<j & i:
                subset.append(set[j])
        ans = add(subset,set)        
    if len(ans)>=1<<N
        return ans
set = input('Enter Elements of set : ').split(sep=' ')
subset = get_subsets(set)
print(subset)
