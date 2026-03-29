class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # create a hashtable to store nodes to their neighbours
        hashmap = defaultdict(list)

        for m in (edges):
            hashmap[m[0]].append(m[1])
            hashmap[m[1]].append(m[0])

        valid = set() # we can have a set of all valid nodes so we dont go over them again
        visited = set()
        print(hashmap)

        def dfs(n,p):        

            #BC if n has been visited 
            if n in visited:
                return False
            #SC
            visited.add(n)
            for i in hashmap[n]:
                if i == p: # becasue it is a parent node, we can skip it
                    continue
                if not dfs(i,n): # call the function again to validate all child nodes
                    return False
            return True
            
        if dfs(0,-1) and len(visited) == n:
            return True
        else:
            return False

       
           
           
            
        

        
      