class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def get_next(self):
    return self.next

  def set_next(self, node):
    self.next = node

class LinkedList:
  def __init__(self, head=None, tail=None):
    self.head = head
    self.tail = tail
  
  def add_to_head(self, value):
    new_head = Node(value, self.head)
    if(self.head == None):
      self.tail = new_head
    self.head = new_head

  def add_to_tail(self, value):
    new_tail = Node(value)
    self.tail.next = new_tail
    self.tail = new_tail

  def delete_from_head(self):
    self.head = self.head.get_next()

  def length(self):
    count = 0
    cur = self.head
    while cur != None:
      count += 1
      cur = cur.get_next()
    return count


class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    self.storage.delete_from_head()
    self.size -= 1

  def len(self):
    return self.storage.length()


