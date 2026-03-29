# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base case 
        if (not p and q) or (p and not q):#if we know not the same structure
            return False
        elif not p and not q: # same structure but just reached leaf node in both
            return True
        elif p.val != q.val:
            return False
            
        
        # step case - if both nodes exists
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
          

