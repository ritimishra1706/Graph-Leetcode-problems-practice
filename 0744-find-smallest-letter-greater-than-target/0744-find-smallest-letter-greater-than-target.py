class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def binary_s(letters,i,j,t):
            n=len(letters)
            ans=""
            while i<=j:
                mid=(i+j)//2
                if letters[mid]<=t:
                    i=mid+1
                elif letters[mid]>t:
                    ans=letters[mid]
                    j=mid-1                   
            return  ans if ans>target else letters[0]                             
        ans=binary_s(letters,0,len(letters)-1,target)
        return ans       