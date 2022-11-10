class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # 데이터를 입력받아 가장앞에 삽입
    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head 
        self.head = new_head

    # 가장 앞에있는 데이터를 꺼내기
    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        deleted_head = self.head
        self.head = self.head.next
        return deleted_head
    
    # 가장앞의 데이터 보기
    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None