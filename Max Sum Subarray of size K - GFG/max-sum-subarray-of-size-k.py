#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
         i=0
         s=0
         j=0
         mx=0
         while j<N:
             if j-i+1<K:
                 s+=Arr[j]
                 j+=1
             elif j-i+1==K:
                 s+=Arr[j]
                 mx=max(mx,s)
                
                 j+=1
             elif j-i+1 >K:
                 s-=Arr[i]
                 s+=Arr[j]
                 mx=max(mx,s)
                 i+=1
                 j+=1
         return mx        
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends