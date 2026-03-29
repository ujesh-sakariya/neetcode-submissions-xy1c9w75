class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            ''' find the root parent of the node '''
            res = n1

            while res != parent[res]: 
             # my code avoids the scenario as we always union with the parent node
             # therefore this loop and optimisation is not needed
             # but if we did not connect to the parent node and we just connected to the node of interest
             # then this loop optimisation is useful as we get to the parent node quicker
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1,n2):
            print(parent)
            p1,p2 = find(n1),find(n2)

            if p1 == p2: # they have the same parent already
                return 0 

            if rank[p2] > rank[p1]:
                parent[p1] = p2 # set the parent to p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            print(parent,'after change')
            return 1

        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)
        
        return res 

            
            

        