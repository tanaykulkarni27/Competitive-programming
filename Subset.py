arr  = [1,2,3,4]
def main(arr):
    subset = []
    find_subset(arr,0,subset)
def find_subset(arr,index,subset):
    if index == len(arr):
        print(subset,end="   ")
    else:
        subset.append(arr[index])
        find_subset(arr,index+1,subset)
        subset.pop(-1)
        find_subset(arr,index+1,subset)        
main(arr)
#  This Solution Implements Recursion to get all the Subsets of given array
