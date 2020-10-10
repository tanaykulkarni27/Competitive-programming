    def binary_search(self,arr,len,i,f):
        mid = (i+len)//2
        if i>len:
            return True
        if arr[mid] == f or arr[len] ==f or arr[0]==f:
            return False
        elif arr[0] ==f:
            return False
        elif arr[mid]>f:
            self.binary_search(arr,mid-1,i,f)
        elif arr[len//2]<f:
            self.binary_search(arr,len,mid+1,f)
