import math
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(m):
            hours = 0

            for p in piles:
                hours += math.ceil(p / m)
            if hours <= h:
                return True
            else:
                return False
                
        
        # max number of valid hours 
        r =  max(piles)
        print('starting r',r)
        # best so far
        best = r
        # min number of hours 
        l = 1

        while l <= r:
            m = (l + r) // 2
            print(m)
            if check(m):
                print('best',best)
                best = min(m,best)
                r = m -1 
            else:
                l = m + 1
        
        return best
            
        


       
                
                

