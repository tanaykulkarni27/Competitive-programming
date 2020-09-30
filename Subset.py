def get_subsets(set):
    subset = [[]]
    for i in range(len(set)):
        copy = subset[:]
        new  = int(set[i])
        for j in range(len(subset)):
             subset[j] = subset[j]+[new]
        subset = subset+copy
    for t in range(len(subset)):
        if len(subset[t]) == 0:
            subset.remove(subset[t])        
    return subset
set = input('Enter Elements of set : ').split(sep=' ')
subset = get_subsets(set)
print(subset)
