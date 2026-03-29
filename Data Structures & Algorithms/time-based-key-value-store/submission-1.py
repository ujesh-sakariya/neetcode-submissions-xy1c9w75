class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        arr = self.time[key]

        l = 0
        r = len(arr) -1
        
        # 2 edge cases
        #1 - if the the value given is bigger than the last item
        #2 - if the value given is less than than the first item 
        while l <= r:
            m = (l+r) // 2
            print(arr,m)
            if arr[m][0] == timestamp:
                return arr[m][1]
            elif arr[m][0] > timestamp:
                r = m - 1
            else:
                l = m  + 1

        # if timestamp is not there we then return the earliest one 
        if not arr or r < 0:
            return ""
        else: return arr[r][1]

        
