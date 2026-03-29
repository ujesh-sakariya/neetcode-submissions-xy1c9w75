class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # monotonic queue - used to keep track of the greatest element in a window 

        q = collections.deque()
        ans = []

        l = r = 0

        while r < len(nums):
            print(r)
            print(l)
            while q and nums[q[-1]] < nums[r]: 
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()

            print(q)
            
            if r - l == k - 1:
                ans.append(nums[q[0]])
            
            r+=1
            if r- l > k-1:
                l+=1
        
        return ans


        