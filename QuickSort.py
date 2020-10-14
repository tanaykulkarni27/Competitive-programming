arr = [2,1,5,4,3]
print('Previous :=-  ',arr)
def partition(arr,l,r):
    pivot = arr[r]
    i = l-1
    for k in range(i+1,r):
        if arr[k]<pivot:
            i+=1
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp
    t = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = t
    return i+1
def QuickSort(arr,l,r):
    if l>r :
        return
    else:
        p = partition(arr,l,r)
        QuickSort(arr,p+1,r)
        QuickSort(arr,l,p-1)
QuickSort(arr,0,len(arr)-1)
print('After Sorting :=-  ',arr)
