
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def Inorder(root1,l):
            if root1==None:
                return
            Inorder(root1.left,l)
            l.append(root1.val)
            Inorder(root1.right,l)
        l1=[]
        l2=[]
        Inorder(root1,l1)
        Inorder(root2,l2)
        n=len(l1)
        m=len(l2)
        i=0
        j=0
        res=[]
        while i<n and j<m:
            if l1[i]<l2[j]:
                res.append(l1[i])
                i+=1
            else:
                res.append(l2[j]) 
                j+=1
        # slicing does not give error if index we are using is out of bound        
        res+=l1[i:]
        res+=l2[j:]        

        '''while i<n:
            res.append(l1[i])
            i+=1
        while j<m:
            res.append(l2[j])
            j+=1'''
        return res                



        