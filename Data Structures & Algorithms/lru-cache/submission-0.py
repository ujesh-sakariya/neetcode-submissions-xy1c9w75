
class node:

    def __init__(self,key,val):
        self.key, self.val = key, val 
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        # internal structure needed
        self.cache = {}
        self.capacity = capacity

        # the 2 dummy pointers needed
        self.left,self.right = node(0,0), node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self,node):
        ''' insert the given node to the end of the linked list '''
        prev = self.right.prev
        prev.next, node.prev  = node, prev
        node.next, self.right.prev = self.right, node

    
    def remove(self,node):
        '''removes the node from the linked list (still in cache)'''
        prev,next = node.prev, node.next
        prev.next, next.prev = next, prev

    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # remove the key and add it so it is now the most recently used
            value = self.cache[key].val
            # node will still be in cache, just removed and re added to linked list 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
            # we create a new node instead of inserting the existing one in case there is a different value being put with it 
        self.cache[key] = node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        

        
