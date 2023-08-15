class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        ind=-1
        for i in range(n-1,0,-1):
            if nums[i]>nums[i-1]:
                ind=i
                break
        if ind-1>=0:             
            x=nums[ind-1]    
        a=nums[ind]
        smallest=-1      
        if ind==-1:
            nums.sort()
       
        else:
            for j in range(ind+1,len(nums)):
                if nums[j]>x and nums[j]<=a:
                    smallest=j  
            if smallest==-1:
                nums[ind],nums[ind-1]=nums[ind-1],nums[ind]
            else:
                nums[smallest],nums[ind-1]=nums[ind-1],nums[smallest]
            # reverse the remaining array    
            i=ind
            j=n-1
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1



        """
        Do not return anything, modify nums in-place instead.
        """