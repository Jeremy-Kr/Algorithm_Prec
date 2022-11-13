class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(value)

    def get_kth_node_from_last(self, k):
        length = 1
        node = self.head
        while node.next is not None:
            node = node.next
            length += 1
        length = length - k
        node = self.head
        for i in range(length):
            node = node.next
        return node

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!