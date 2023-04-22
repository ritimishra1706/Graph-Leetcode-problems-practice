# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        q=[[root,0,0]]
        mx=0
        while q:
            x,y,z=q.pop(0)
            mx=max(mx,y)
            if x==None:
                continue
            if z==1:
                q.append([x.left,1,1])
            else:
                q.append([x.left,y+1,1])
            if z==2:
                q.append([x.right,1,2])
            else:
                q.append([x.right,y+1,2])
             
        return mx-1    

        
            
        