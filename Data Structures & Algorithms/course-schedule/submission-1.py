class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        def dfs(course):

            #BC - if the node has already been visited
            if course in visited:
                return False
            #BC - if the course has no pre, then we know it is valid
            if map[course] == []:
                return True
            
            #SC
            visited.add(course)
            for pre in map[course]:
                if not dfs(pre):
                    return False
            visited.remove(course) # because we are done, we need to remove it so it doesnt conflict with other nodes that might have this as a pre req
            map[course] = [] # we set it to that as it prevents us having to validate the course again 
            return True
            
        # first create the hashtable 
        map = defaultdict(list)
        for p in prerequisites:
            map[p[0]].append(p[1])
        
        #set to store all the courses along the DFS path
        visited = set()

        for i in range(numCourses):
            if not dfs(i):
                return False
        else:
            return True

        

        
        

            
            
