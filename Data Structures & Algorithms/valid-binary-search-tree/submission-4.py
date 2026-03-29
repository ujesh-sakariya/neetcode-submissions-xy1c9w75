# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root,l,u):
            #BC
            if not root:
                return True

            if root.val <=  l or root.val >= u:
                return False
                    
    
            
            #SC
            
            return valid(root.left,l,root.val) and valid(root.right,root.val,u)
        
        return valid(root,-1001,1001)