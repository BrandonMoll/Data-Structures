"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_head = ListNode(value, None, self.head)
    if self.head:
      self.head.insert_before(new_head)
    if not self.tail:
      self.tail = new_head
    self.head = new_head
    self.length += 1
    pass

  def remove_from_head(self):
    old_head = self.head.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.head = self.head.next
      self.head.prev.delete()
      self.length -= 1

    return old_head

  def add_to_tail(self, value):
    new_tail = ListNode(value, self.tail, None)
    if self.tail:
      self.tail.next = new_tail
    if self.head == None:
      self.head = new_tail
    self.tail = new_tail
    self.length += 1


  def remove_from_tail(self):
    removed = self.tail.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.tail = self.tail.prev
      self.tail.next.delete()
    return removed

  def move_to_front(self, node):
    if self.tail == self.head:
      pass
    else:
      node.prev.next = node.next
      if node != self.tail:
        node.next.prev = node.prev
      node.next = self.head
      node.prev = None
      self.head = node
      

  def move_to_end(self, node):
    if self.tail == self.head:
      pass
    elif node == self.tail:
      pass
    elif node == self.head:
      new_tail = node
      self.remove_from_head()
      self.add_to_tail(new_tail.value)
    else:
      node.prev.next = node.next
      node.next.prev = node.prev
      node.next = None
      node.prev = self.tail
      self.tail = node
      

  def delete(self, node):
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    if node == self.head:
      self.remove_from_head()
    if node == self.tail:
      self.remove_from_tail()
    else:
      node.delete()
    
  def get_max(self):
    current = self.head
    cur_max = 0
    while current != None:
      if current.value > cur_max:
        cur_max = current.value
      current = current.next
    return cur_max


