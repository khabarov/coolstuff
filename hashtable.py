class Element:
     def __init__(self, key, value):
          #Linked list
          self.key = key
          self.value = value
          self.next = None 
     def get_key(self):
          return self.key
     def get_value(self):
          return self.value
     def set_nxt(self, element):
          self.next = element

#Division method with chaining
class Hashtable:
     def __init__(self):
          self.array = [None] * 8
          self.size = len(self.array)
          self.count = 0
          self.base = 256
          
      
     def _check_load(self):
          if self.count <= (self.size/4):
               #shrink
               array = [None] * (self.size/2)
               self.size = len(array)
               self._rehash(array)
          elif self.count > self.size:
               #double
               array = [None] * (self.size*2)
               self.size = len(array)
               self._rehash(array)
               #reinsert each Element into a new array
           
                
     def insert(self, key, value):
          #check the load factor
          self.count+=1
          self._check_load()
          index = self._hash(key)
          element = Element(key, value)
          slot = self.array[index]
          if (slot == None):
               self.array[index] = element
          else:
               while slot.next != None and slot.key != key:
                    slot = slot.next
               if (slot.key == key):
                    slot.value = value
               else:
                    slot.next = element # or slot.set_nxt(element)
                    
     def delete(self, key):
          self.get(key) #checking if key is in the table
          index = self._hash(key)
          slot = self.array[index]
          # assuming there isn't going to be a miss (i.e. key is guranteed to be in this linked list)
          prev = None
          while slot.key != key:
               prev = slot
               slot = slot.next
          if prev == None:
               self.array[index] = None
          else:
               prev.next = slot.next
               slot.next = None #don't really need this
          self.count-=1
          self._check_load()          

                    
     def get(self, key):
          index = self._hash(key)
          slot = self.array[index]
          if (slot == None):
                raise KeyError("Invalid key")
          else:
               while slot.next != None and slot.key != key:
                    slot = slot.next
               if (slot.key == key):
                    return slot.value
               else:
                    raise KeyError("Invalid key")           
                             
     def _rehash(self, new):
          #reinsert each Element into a new array (change self.size)
          for i in self.array:
               while i != None:
                    index = self._hash(i.key)
                    element = Element(i.key, i.value)
                    slot = new[index]
                    if (slot == None):
                         new[index] = element
                    else:
                         while slot.next != None:
                              slot = slot.next
                         slot.next = element
                    i=i.next
          self.array = new
          
     def _hash(self, key):
          hash = 0
          if type(key) is int:
                hash = key % self.size
          elif type(key) is str:
                for c in key:
                    hash = (hash * self.base + ord(c)) % self.size
          else:
                raise KeyError("Cannot insert key")  
          return hash
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
hahstable class:
 hashtable list/array
 array size
 # of elements
 add()
   call hash function: get position in hashtable
   insert into hahstable (last element in the linked list)
   increate # of elements ->check load factor
     
 remove()
    search(key, remove flag)
 search(key)
    if no remove flag:
        return value
    else:
        change pointers in the linked list
        decreate # of elements
        check load factor
 check load factor()
    resize if necessary
 resize()
   increase/decrease array size: set m() in hash fucntion if necessary->rehash
 rehash()

element class:
 key
 value
 next

hash function class:
 hash function
 set m()
 '''
