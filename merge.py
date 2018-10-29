
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.item)
            printval = printval.next

    def bubblesort(self):
        current = self.head
        while current is not None:
            previous = current.next
            while previous != None:
                if previous.item < current.item:
                    temp = current.item
                    
                    current.item = previous.item
                    previous.item = temp

                previous = previous.getNext()
            current = current.getNext()
    def AppendNode(self, item):
        new_node = Node(item)

        if self.head == None:
            self.head = new_node

        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node
    def duplicate(self):
        current = self.head
        for i in range (6000):

            for j in range (6000):
                if self.head == current.next:
                    print(current.next.item)

                    current = current.next
            self.head = self.head.next
my_list = LinkedList()
with open('activision.txt','r') as file:
    list1 = LinkedList()

    for line in file:
        list1.AppendNode(line)
with open('vivendi.txt', 'r') as file:
    list2 = LinkedList()

    for line in file:
        list2.AppendNode(line)
list1.tail.next = list2.head
last = list1.tail.next
h = list1.head
#print(list1.tail.next.next.item)
list1.head.item
for i in range (0,6000):
    my_list.AppendNode(list1.head.item)
    list1.head = list1.head.next
my_list.listprint()

