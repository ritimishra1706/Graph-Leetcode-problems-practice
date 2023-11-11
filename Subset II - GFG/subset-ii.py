#User function Template for python3

class Solution:
    def printUniqueSubset(self, nums):
        def solve(ind,nums,res,final):
            final.append(res[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                res.append(nums[i])
                solve(i+1,nums,res[:],final)
                res.pop()
        res=[]
        final=[]
        nums.sort()
        ind=0
        solve(ind,nums,res,final)
        return final
            
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.printUniqueSubset(nums)
        print('[ ', end = '')
        for subset in res:
            print('[ ', end = '')
            for val in subset:
                print(val, end = ' ')
            print(']', end = '')
        print(' ]')
# } Driver Code Ends