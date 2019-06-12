class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current = self
    target = value
    complete = False

    while not complete:

      if target < current.value:
        if current.left:
          current = current.left
        else:
          current.left = BinarySearchTree(target)
          complete = True

      if target > current.value:
        if current.right:
          current = current.right
        else:
          current.right = BinarySearchTree(target)
          complete = True

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass
