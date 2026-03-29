# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        m = 0
        def dfs(root):
            nonlocal m
            #BC
            if not root:
                return -1
            
            #SC
            
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            m = max(m,(left+right))
            return max(left,right)

        dfs(root)
        return m


