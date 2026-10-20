#Class Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.num = 0

    def add_first(self,value):
        n_node = Node(value)
        n_node.next = self.head
        self.head = n_node
        self.num += 1

    def add_last(self,value):
        n_node = Node(value)
        cur = self.head
        for i in range(1,self.num):
            cur = cur.next
        cur.next = n_node
        self.num += 1

    def add_position(self,value,position):
        n_node = Node(value)
        cur = self.head
        for i in range(1,position-1):
            cur = cur.next
        n_node.next = cur.next
        cur.next = n_node
        self.num += 1

    def delete_frist(self):
        self.head = self.head.next
        self.num -= 1
            
    def delete_last(self):
        cur = self.head
        for i in range(1,self.num-1):
            cur = cur.next
        cur.next = None

    def delete_position(self,position):
        cur = self.head
        for i in range(1,position-1):
            cur = cur.next
        cur.next = cur.next.next

    def update(self,value,position):
        cur = self.head
        for i in range(1,position):
            cur = cur.next
        cur.data = value

    def search(self,value):
        cur = self.head
        for position in range(1,self.num):
            if cur.data == value:
                return position
            cur = cur.next
        return "Not Found"

    def display(self):
        output = 'head-->'
        cur = self.head
        while cur:
            output += f'{cur.data}-->'
            cur = cur.next
        output += 'None'
        return output

link = LinkedList()
link.add_first('D')
link.add_first('C')
link.add_first('B')
link.add_first('A')
while True:
    print(link.display())
    print(f'''======== LinkedList ========
Type :  1-Add 2-Delete 3-Update 4-Search 5-Exit''')
    choice = input('Choose : ')
    match choice:
        case '1':
            print('''Which one do you want?
1-Add Frist
2-Add Last
3-Add Position
4-Skip''')
            choice2 = input('Choose : ')
            match choice2:
                case '1':
                    value = input('Input value : ')
                    link.add_first(value)
                case '2':
                    value = input('Input value : ')
                    link.add_last(value)
                case '3':
                    position = int(input('Input position that you want to add : '))
                    value = input('Input value : ')
                    link.add_position(value,position)
                case '4':
                    continue
                case _:
                    print('Invaild Input !!')
        case '2':
            print('''Which one do you want?
1-Delete Frist
2-Delete Last
3-Delete Position
4-Skip''')
            choice2 = input('Choose : ')
            match choice2:
                case '1':
                    link.delete_frist()
                case '2':
                    link.delete_last()
                case '3':
                    position = int(input('Input position that you want to delete : '))
                    link.delete_position(position)
                case '4':
                    continue
                case _:
                    print('Invaild Input !!')
        case '3':
            position = int(input('Input position that you want to uodate : '))
            value = input('Input value : ')
            link.update(value,position)
        case '4':
            value = input('Input value that you want to search : ')
            print('Result : ',end='')
            print(link.search(value))
        case 5:
            print('Byebye !!')
            break
        case _:
            print('Invaild Input !!!')
            