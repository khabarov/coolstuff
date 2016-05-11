class PriorityQueue:
    """Array-based priority queue implementation."""
    def __init__(self):
        """Initially empty priority queue."""
        self.queue = []
        self.min_index = 0
    
    def __len__(self):
        # Number of elements in the queue.
        return len(self.queue)
    
    def append(self, key):
        """Inserts an element in the priority queue."""
        parent_index = None
        if key is None:
            raise ValueError('Cannot insert None in the queue')
        if len(self.queue) == 0:
            self.queue.append(key) 
        else:
            self.queue.append(key)
	    key_index = len(self.queue)-1
            swapped = True
            
            while swapped == True and key_index is not 0:
                # get the index of the parent
                if key_index%2 == 0:
                    parent_index = (key_index/2)-1
                elif key_index%2 == 1:
                    parent_index = key_index/2    
                #bubble up
                if (key<self.queue[parent_index]):
                    temp = self.queue[parent_index]
                    self.queue[parent_index] = key
                    self.queue[key_index] = temp
		    key_index = parent_index
                else:
                    swapped = False 
        #self.min_index = None
    
    def min(self):
        """The smallest element in the queue."""
        if len(self.queue) == 0:
            return None
        #self._find_min()
        return self.queue[self.min_index]
    
    def pop(self):
        """Removes the minimum element in the queue.
    
        Returns:
            The value of the removed element.
        """
        popped_key = None
        if len(self.queue) == 0:
            return None
        elif len(self.queue) == 1:
            popped_key = self.queue.pop(self.min_index)
        else:
            popped_key = self.queue[self.min_index]
            self.queue[self.min_index] = self.queue[-1]
            self.queue.pop(-1)
            self._min_heapify(self.min_index)
        #self.min_index = None
        return popped_key
    
    def _min_heapify(self,i):
        # Computes the index of the minimum element in the queue.
        #
        # This method may crash if called when the queue is empty.
        
        smallest = None
        l = None
        r = None
        if (i == 0):
            l = 1
            r = 2
        else:
	    l = (2*i)+1;
	    r = (2*i)+2;            
        if (l<len(self.queue) and self.queue[l] < self.queue[i]):
	    smallest = l
	else:
	    smallest = i
	if (r<len(self.queue) and self.queue[r] < self.queue[smallest]):
	    smallest = r
	
	if (smallest is not i):
	    temp = self.queue[i]
	    self.queue[i] = self.queue[smallest];
	    self.queue[smallest] = temp;
	    self._min_heapify(smallest)

        #if self.min_index is not None:
            #return
        #min = self.queue[0]
        #self.min_index = 0
        #for i in xrange(1, len(self.queue)):
            #key = self.queue[i]
            #if key < min:
                #min = key
                #self.min_index = i


queue = PriorityQueue()
queue.append(5)
queue.append(8)
queue.append(10)
queue.append(3)
queue.append(1)
queue.append(15)
queue.append(2)
queue.append(9)
queue.append(3)
queue.append(4)

print queue.queue

queue.pop()
print queue.queue
queue.pop()
print queue.queue
queue.pop()
print queue.queue
queue.pop()
print queue.queue
queue.pop()
print queue.queue
queue.pop()
queue.append(4)
print queue.queue
queue.pop()
print queue.queue
queue.pop()
print queue.queue
queue.pop()
print queue.queue
queue.pop()
#min_num = queue.pop()
print queue.queue