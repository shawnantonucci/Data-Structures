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
        # pass
        new_node = ListNode(value)
        temp_node = self.head

        self.head.insert_before(new_node)
        self.head = new_node
        self.head.next = temp_node

    def remove_from_head(self):
        # pass
        temp_node = self.head.value
        return temp_node

    def add_to_tail(self, value):
        # pass
        new_node = ListNode(value)
        self.tail.insert_after(new_node)
        self.tail = new_node

    def remove_from_tail(self):
        # pass
        temp_node = self.tail.value
        self.tail.delete()
        return temp_node

    def move_to_front(self, node):
        # pass
        node.delete
        self.add_to_head(self, node.value)

    def move_to_end(self, node):
        # pass
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def delete(self, node):
        # pass
        next_node = node.next
        prev_node = node.prev

        prev_node.next = next_node
        next_node.prev = prev_node

    def get_max(self):
        pass
        current_node = self.head
        max_value = 0
        if current_node != None:
            while current_node != None:
                temp_value = current_node.get_value()
                if temp_value > max_value:
                    max_value = temp_value
                else:
                    current_node = current_node.get_next()
            return max_value
