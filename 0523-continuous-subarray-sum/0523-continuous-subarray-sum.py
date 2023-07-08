class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={}
        s=0
        d[0]=0 
        for i in range(len(nums)):
            s+=nums[i]
            if s%k not in d:
                d[s%k]=i+1
            else:
                if i>d[s%k]:
                    return True
        return False              

        