import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        maps = defaultdict(list)

        for p in points:
            print('current p', p)
            d = -(math.sqrt(p[0]**2 + p[1]**2))
            if len(heap) < k:
                heapq.heappush(heap,d)
                maps[d].append(p)
            elif d > heap[0]:
                heapq.heappush(heap,d)
                heapq.heappop(heap)
                maps[d].append(p)
                print(p)
                print(maps)
        
        arr = []
        for _ in range(k):
            t = heapq.heappop(heap)
            print(maps)
            arr.append(maps[t][0])
            maps[t].pop(0)
        
        return arr


            

        