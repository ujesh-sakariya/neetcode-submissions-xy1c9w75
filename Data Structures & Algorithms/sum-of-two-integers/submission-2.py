class Solution:
    def getSum(self, a: int, b: int) -> int:
        # let b contain the AND
        # let a contain the XOR
        # with python, integers are arbitary sizes while in languages like java, they are 32 bits long
        
        # in python they store negative numbers with sign and magnitude
        # when you use bitwise operations, it converts it into 2's compliment
        # but without a fixed size  (infinite 1's to the left does not change the value)
        # therefore to get it to work, you need to mask the value into 32 bit values so there is a cut off
        # boolean operations require fixed-widths to work

        mask = 0xFFFFFFFF # cut off at 32 bits
        max_pos = 0x70000000 # 0 (pos) followed by 1's

        while b!=0:

            cppy = a 
            a = (a ^ b) & mask # this extract only the first 32 bits and sets rest to 0
            b = (cppy & b) << 1 & mask # this ensure as you shift left, eventually it becomes all 0's instead of growing infintly long
        
        # if by the end we have a number 1...
        # this means it must be negative number therefore return the negative answer
        if a > max_pos:
        # we need to return it as sign and magnitude to do so we first need to find the magnitude
         # to go from pos to neg we flip all bits add 1
            a = a ^ mask # this flips all bits so the too big pos number is now actually the negative number
            a = ~a # this performs NOT which negates (a + 1) therfore return the correct answer
        else:
            return a


        return a
            
        