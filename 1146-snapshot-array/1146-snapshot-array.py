class SnapshotArray:
    # you have to take snapshot of the array everytime when you set an element
    # so if you will choose a hashmap of every indexs and at each index you shuld
    # take a second map where key is the snapid and value is the that value which we have
    # to set at that index

    def __init__(self, length: int):
        self.length=length
        self.d1={}
        self.snapid=0
        
        for i in range(self.length):
            # d2 stores key as a snapid and value as val
            d2={}
            d2[0]=0
            self.d1[i]=d2
        

    def set(self, index: int, val: int) -> None:
        self.d1[index][self.snapid]=val
        
    def snap(self) -> int:
        self.snapid+=1
        return self.snapid-1
        

    def get(self, index: int, snap_id: int) -> int:
        # arrays of snapId
        arr=list(self.d1[index].keys())
        n=len(arr)
        l=0
        r=n-1
        # if given snapid is not found return just smaller snapid
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==snap_id:
                res=arr[mid]
                break
            elif arr[mid]<snap_id:
                res=arr[mid]
                l=mid+1
            else:
                r=mid-1
        return self.d1[index][res]                
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)