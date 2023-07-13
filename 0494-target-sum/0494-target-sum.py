class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # top down dp
        # time complexity= min(2^n , n*sum)
        dp={} # (index,totalsum)
        # index - range -(0,len(nums))
        # totalsum- range-(sum,+sum)= 1+2*sum
        def dp_solve(i,totalsum):
            if i==len(nums):
                if totalsum==target:
                    return 1
                else:
                    return 0
            if (i,totalsum) in dp:
                return dp[(i,totalsum)]
            dp[(i,totalsum)]=dp_solve(i+1,totalsum+nums[i])+dp_solve(i+1,totalsum-nums[i]) 
            return dp[(i,totalsum)]            
        return dp_solve(0,0)