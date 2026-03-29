class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0 # just think of this as 32 0's
        for i in range(32):
            bit = n & 1
            n = n >> 1
            res = res | (bit << (31 - i)) # we are shifting the bit to the right so it aligns

        return res