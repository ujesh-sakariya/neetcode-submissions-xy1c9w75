"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        hasht = {}
        def dfs(v):
            nonlocal hasht
            #BC
            # if the node exists in hash table, return it 
            if v.val in hasht:
                return hasht[v.val]

            #SC
            # if the node does not exist, clone it 
            if v.val not in hasht:
                curr = Node(v.val)
                hasht[v.val] = curr
                for n in v.neighbors:
                    curr.neighbors.append(dfs(n))
            return curr
        
        return dfs(node)





                
                

