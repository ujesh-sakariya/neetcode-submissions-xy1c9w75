# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = k # count down the number of nodes
        res = root.val # placehilder for the answer
        def inOrder(root):
            
            nonlocal count,res # allow you to modify the outer variables
            #BC
            if not root:
                return False # not found yet
            
            

            #SC

            if inOrder(root.left): # if it returns True, it means it is found
                return True

            count-=1
            if count == 0:
                res = root.val
                return True
            if inOrder(root.right):
                return True
            
            return False

            


        inOrder(root)
        return res

        