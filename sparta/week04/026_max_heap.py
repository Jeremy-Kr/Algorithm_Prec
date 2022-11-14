class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        curr_idx = len(self.items)-1

        while curr_idx > 1:
            parent_idx = curr_idx // 2
            if self.items[curr_idx] > self.items[parent_idx]:
                self.items[curr_idx],self.items[parent_idx] = self.items[parent_idx],self.items[curr_idx]
                curr_idx = parent_idx
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!