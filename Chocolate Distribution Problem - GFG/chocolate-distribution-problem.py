#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        min_diff=float('inf')
        for i in range(N-M+1):
            # jump from i to m step
            min_diff=min(min_diff,A[i+M-1]-A[i])
        return min_diff        

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends