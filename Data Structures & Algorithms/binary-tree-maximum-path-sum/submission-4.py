# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxC = -100000
        def calc(root):
            nonlocal maxC
            #BC
            if not root:
                return -10000
            
            #SC
            l = calc(root.left)
            r = calc(root.right)
            maxC = max(maxC,root.val,r+l+root.val,r+root.val,l+root.val)
            print(maxC)
            print('with',root.val,max(root.val,r+l+root.val,r+root.val,l+root.val))
            return max(root.val,r+root.val,l+root.val)

        calc(root)
        return maxC

        

