class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.num = 0

    def add_first(self, value):
        n_node = Node(value)
        n_node.next = self.head
        self.head = n_node
        self.num += 1

    def add_last(self, value):
        if self.head is None:
            return self.add_first(value)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)
        self.num += 1

    def add_position(self, value, position):
        if position < 1 or position > self.num + 1:
            return False
        if position == 1:
            self.add_first(value)
            return True
        cur = self.head
        for _ in range(position - 2):
            cur = cur.next
        n_node = Node(value)
        n_node.next = cur.next
        cur.next = n_node
        self.num += 1
        return True

    def delete_first(self):
        if self.head is None:
            return False
        self.head = self.head.next
        self.num -= 1
        return True

    def delete_last(self):
        if self.head is None:
            return False
        if self.num == 1:
            return self.delete_first()
        cur = self.head
        for _ in range(self.num - 2):
            cur = cur.next
        cur.next = None
        self.num -= 1
        return True

    def delete_position(self, position):
        if position < 1 or position > self.num:
            return False
        if position == 1:
            return self.delete_first()
        cur = self.head
        for _ in range(position - 2):
            cur = cur.next
        cur.next = cur.next.next
        self.num -= 1
        return True

    def update(self, value, position):
        if position < 1 or position > self.num:
            return False
        cur = self.head
        for _ in range(position - 1):
            cur = cur.next
        cur.data = value
        return True

    def search(self, value):
        cur = self.head
        for position in range(1, self.num + 1):
            if cur.data == value:
                return position
            cur = cur.next
        return None

    def display(self):
        output = 'head-->'
        cur = self.head
        while cur:
            output += f'{cur.data}-->'
            cur = cur.next
        return output + 'None'