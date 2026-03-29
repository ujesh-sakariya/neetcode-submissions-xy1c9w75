class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        p = 0
        b = prices[0]

        for i in range(1,len(prices)):

            if prices[i] - b > p:
                p = prices[i] - b
            if prices[i] < b:
                b = prices[i]

        return p 
        