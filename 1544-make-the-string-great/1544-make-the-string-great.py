class Solution:
    def makeGood(self, s: str) -> str:
        # Using Stack
        stack=[]
        for i in s:
            if stack and abs(ord(stack[-1])-ord(i))==32:
                stack.pop()
            else:
                stack.append(i)
    
        ans=''.join(stack)
        return ans            
        