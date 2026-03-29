import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        print(stones)
        heapq.heapify(stones)

        print(heapq)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x,y)
            if x != y:
                heapq.heappush(stones,(x-y))

        return -(heapq.heappop(stones)) if stones else 0