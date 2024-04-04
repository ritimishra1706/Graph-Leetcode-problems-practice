class Solution:
    def maxDepth(self, s: str) -> int:
        # "(" this will increase depth and ')' will less depth of next element
        # maintain the max depth
        c=0
        m=0
        for i in s:
            if i=='(':
                c+=1
            elif i==')':
                c-=1
            m=max(c,m) 
        return m           
        