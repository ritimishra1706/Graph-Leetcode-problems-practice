#User function Template for python3
class Solution:
    def solve(self,arr,i,sub,output):
        if i>=len(arr):
            s=sum(sub)
            output.append(s)
            return
        sub.append(arr[i])
        self.solve(arr,i+1,sub,output)
        sub.pop()
        self.solve(arr,i+1,sub,output)
    def subsetSums(self,arr,N):
        output=[]
        sub=[]
        i=0
        self.solve(arr,i,sub,output)
        output.sort()
        return output
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends