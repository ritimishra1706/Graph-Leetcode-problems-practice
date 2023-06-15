# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        m=-float('inf')
        levelcount=0
        smallestlevel=0
        while q:
            level=len(q)
            s=0
            levelcount+=1
            for i in range(level):
                x=q.popleft()
                s+=x.val
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            if s>m:
                m=s
                smallestlevel=levelcount
        return smallestlevel   




          