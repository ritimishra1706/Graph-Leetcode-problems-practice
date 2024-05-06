class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def solve(str1,str2):
            n=len(str1)
            m=len(str2)
            i=0
            j=0
            res=""
            while i<n and j<m:
                if str1[i]!=str2[j]:
                    break
                res+=str1[i]
                i+=1
                j+=1
            return res        
        prefix=strs[0]
        for i in range(1,len(strs)):
            prefix=solve(prefix,strs[i])
        return prefix    

        