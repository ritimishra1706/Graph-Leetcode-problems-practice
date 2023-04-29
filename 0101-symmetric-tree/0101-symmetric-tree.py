# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(t1,t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            else:
                return t1.val==t2.val and solve(t1.left,t2.right) and solve(t1.right,t2.left)
        return solve(root,root)    
                
        