import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # heap for maintiaining which letter to prioritise
        # hash map mapping letter to last cycle
        # we can remove an item from the heap 
        # decrement the counter of how many we have left
        # update the cooldown hash map
        # mapping of how many are left

        queue = []

        cycles = 0
        # count how many of each letter we have
        freq = {}
        for letter in tasks:
            freq[letter] = 1 + freq.get(letter,0)

        heap = []
        # put in a 2d array so can put in a heap
        for key,value in freq.items():
            heap.append([-value,key])

        # Create a heap to store the priority
        heapq.heapify(heap)
        # while the heap is not empty
        while heap or queue:
            cycles +=1
            if heap:
                task = heapq.heappop(heap)
                if task[0] != -1:
                    queue.append([cycles,task[0]+1,task[1]])
          
            
        
            # adding eleemnt back to the queue if appropriate

            if queue and cycles - queue[0][0] >= n:
                curr = queue.pop(0)
                heapq.heappush(heap,curr[1:])
            print(cycles)
            print(heap)
            print(queue)
        
        return cycles
                
                    




            