class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[0])
        print(intervals)
        output =[intervals[0]]

        for s,e in intervals[1:]:

            prev = output[-1]

            if prev[1] > s:
                # starting at same value
                if prev[0] == s:
                    output[-1] = prev if abs(prev[1] - prev[0]) <= abs(e -s) else [s,e]
                # curr is a sub array of prev
                elif prev[0] < s and prev[1] > e:
                        output[-1] = [s,e]
            else:
                output.append([s,e])
        
        return len(intervals) - len(output)

        