class MinStack:

    def __init__(self):
        self.s = []
        self.tops = []
    def push(self, val: int) -> None:
    
        self.s.append(val)

        # check if it should be added to max
        if len(self.tops) != 0:
            if self.tops[-1] >= val:
                self.tops.append(val)
        else:
            self.tops.append(val)
            

    def pop(self) -> None:
        x = self.s.pop()
        if self.tops[-1] == x:
            self.tops.pop()
        

    def top(self) -> int:
        if self.s:
            return self.s[-1]
        

    def getMin(self) -> int:
        print(self.tops)
        return self.tops[-1]
        

        
