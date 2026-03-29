class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        hash = [[position[i],speed[i]] for i in range(len(position))]

        hash = sorted(hash,key = lambda x:x[0])
        print(hash)

        fleet = 0
        p =-1
        while hash:
            c = hash.pop()
            estimate = (target - c[0]) / c[1]
            print(p,estimate)
            if estimate > p:
                print(c)
                fleet+=1
                p = estimate
        
        return fleet
