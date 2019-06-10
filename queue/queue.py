class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    pass
    self.storage.append(item)

  def dequeue(self):
    pass
    if len(self.storage) > 0:
      return self.storage.pop(0)

  def len(self):
    pass
    return len(self.storage)
