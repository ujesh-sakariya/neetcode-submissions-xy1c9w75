import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
       

        for p in points:
            print('current p', p)
            d = -(math.sqrt(p[0]**2 + p[1]**2))

            if len(heap) < k:

                heapq.heappush(heap,[d,[p[0],p[1]]])
            elif d > heap[0][0]:
                heapq.heappush(heap,[d,[p[0],p[1]]])
                heapq.heappop(heap)
        
        arr = []
        for _ in range(k):
            t = heapq.heappop(heap)
            print(t)
            arr.append(t[1])
    
        
        return arr


            

        