class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 1
        i=0     
        nums.sort()
        m=0
        c=1
        diff=0
        for j in range(1,len(nums)):
            diff+=(nums[j]-nums[j-1])*c
            while i<len(nums) and diff>k:
                diff-=nums[j]-nums[i]
                i+=1
                c-=1
            c+=1 
            m=max(m,c)
        return m    


                
           