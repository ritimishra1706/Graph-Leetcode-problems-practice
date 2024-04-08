class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n=len(s)
        ans=[""]*n
        stack=[]
        for i in range(n):
            if s[i]=='(':
                stack.append([s[i],i])
            elif s[i]==')':
                if not stack:
                    ans[i]=""
                elif stack[-1][0]=='(':
                    chr,ind=stack.pop()
                    ans[ind]=chr
                    ans[i]=s[i]
            else:
                ans[i]=s[i]
        #print(ans)     
        return ''.join(ans)           

        