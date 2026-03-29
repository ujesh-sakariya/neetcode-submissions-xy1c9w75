import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        for n in nums:
            print(n,nums[0])
            if len(heap) < k:
                heapq.heappush(heap,n)
           
            elif n > heap[0]:
                heapq.heappush(heap,n)
                heapq.heappop(heap)
            print(heap)
        return heap[0]
        
        