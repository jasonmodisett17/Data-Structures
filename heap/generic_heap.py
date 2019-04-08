class Heap:
  def __init__(self, comparator=lambda x, y: x > y):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    new_index = len(self.storage)
    self.storage.append(value)
    self._bubble_up(new_index)

  def delete(self):
    if len(self.storage) == 0:
      return None
    elif len(self.storage) == 1:
      temp = self.storage[0]
      self.storage = []
      return temp

    last_index = len(self.storage) - 1
    self.storage[0], self.storage[last_index] = self.storage[last_index], self.storage[0]

    temp = self.storage.pop(last_index)

    self._sift_down(0)

    return temp

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    found_spot = False

    while not found_spot:
      parent_index = (index - 1) // 2

      if parent_index < 0:
        parent_index = 0

      if self.comparator(self.storage[index], self.storage[parent_index]):
        self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
        index = parent_index
      else:
        found_spot = True

  def _sift_down(self, index):
    found_spot = False

    while not found_spot:
      child1_index = (index * 2) + 1
      child2_index = (index * 2) + 2

      if child1_index > len(self.storage) - 1:
        largest_child_index = index

      elif child2_index > len(self.storage) - 1:
        largest_child_index = child1_index

      elif self.comparator(self.storage[child1_index], self.storage[child2_index]):
        largest_child_index = child1_index
      else:
        largest_child_index = child2_index

      if self.comparator(self.storage[largest_child_index], self.storage[index]):
        self.storage[index], self.storage[largest_child_index] = self.storage[largest_child_index], self.storage[index]
        index = largest_child_index
      else:
        found_spot = True