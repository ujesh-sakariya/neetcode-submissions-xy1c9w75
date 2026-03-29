class node:
    def __init__(self,value=0,key=0):
        self.right = None
        self.left = None
        self.value = value
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = node()
        self.tail = node()
        self.head.left,self.tail.right = self.tail, self.head

        self.mapping = {}

    def get(self, key: int) -> int:
        if key in self.mapping: 
            self.delete(self.mapping[key])
            self.add(self.mapping[key])
            return self.mapping[key].value
        else: return -1


    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.delete(self.mapping[key])

        n = node(value,key)
        self.add(n)
            # update the value
        self.mapping[key] = n
          
        if len(self.mapping) > self.capacity:
                lru = self.tail.right.key
                self.delete(self.tail.right)
                del self.mapping[lru]
                
        


    def add(self,node):
        node.left = self.head.left
        self.head.left.right = node
        self.head.left = node
        node.right = self.head
    
    def delete(self,node):

        node.left.right = node.right
        node.right.left = node.left
        

        
