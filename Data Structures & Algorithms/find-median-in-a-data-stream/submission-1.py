class MedianFinder:

    def __init__(self):
        
        self.small = [] # small heap    
        self.large = [] # large heap
    def addNum(self, num: int) -> None:

        # 1 default add to small heap
        heapq.heappush(self.small,-1 * num) # python doe not allow the implementation for max heap, therefore you need to us -1* 

        # 2 make sure every element in small is smaller than large
        if self.small and self.large and -1 * self.small[0] >  self.large[0]: # check that they are not empty arrays
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        # 3 ensure that the size is approx the same 
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        
        elif len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small,val) 


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1* self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] + -1*self.small[0]) / 2

        
        