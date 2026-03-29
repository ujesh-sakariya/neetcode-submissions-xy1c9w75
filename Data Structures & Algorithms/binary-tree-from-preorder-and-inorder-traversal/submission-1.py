# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # create hash map 
        hash = {}
        for i,v in enumerate(inorder):
            hash[v] = i


        def dfs(l,r):
            #bc
            if l > r:
                return None
    
        
        
            #sc
            root = TreeNode()
            c = preorder.pop(0)
            root.val = c

           

            root.left = dfs(l,hash[c]-1)
            root.right = dfs(hash[c]+1,r)
            return root

        return dfs(0,len(inorder)-1)




            


        