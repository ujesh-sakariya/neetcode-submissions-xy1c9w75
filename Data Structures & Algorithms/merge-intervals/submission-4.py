class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        
        intervals.sort(key=lambda x:x[0])
        output = [intervals[0]]
        
        for s,e in intervals[1:]:
            l = output[-1][1]

            if s <= l:
                output[-1][1] = max(e,l)
            else:
                output.append([s,e])
        
        return output 

            
            
        