#%%
from requests.api import delete


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_at_beginning(self, node: str):
        prev_head = self.head
        self.head = Node(data=node)
        self.head.next = prev_head

    def add_at_end(self, node: str):
        if self.head is None:
            self.head = Node(data=node)
            return
        for current_node in self:
            pass

        current_node.next = Node(data=node)

    def add_after(self, node: str, new_node: str):
        if self.head is None:
            raise Exception("List is empty")
        
        new_node = Node(data=new_node)
        
        for current_node in self:
            if current_node.data == node:
                new_node.next = current_node.next
                current_node.next = new_node
                return
        raise Exception("Node not found")
    
    def add_before(self, node: str, new_node: str):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == node:
            self.add_at_beginning(new_node)
            return

        new_node = Node(data=new_node)
        prev_node = self.head
        for current_node in self:
            if current_node.data == node:
                prev_node.next = new_node
                new_node.next = current_node
                return
            prev_node = current_node

        raise Exception("Node not found")
    
    def remove_node(self, node: str):
        if self.head is None:
            raise Exception("List is empty")

        #remove if node easily if start of the list
        if self.head.data == node:
            self.head = self.head.next # remove head
            return
        
        prev_node = self.head
        for current_node in self:
            if current_node.data == node:
                prev_node.next = current_node.next
                return
            prev_node = current_node
        
        raise Exception("Node not found")
# %%
first_node = Node('a')
print(first_node.next)
# %%
llist = LinkedList() # Right now, linked list is empty.

first_node = Node('a') # Now, 'a' is the first node in our linked list.
llist.head = first_node
print(llist)
# %%
second_node = Node('b') # 'b' is the second node in our linked list.
third_node = Node('c') # 'c' is the third node in our linked list.
first_node.next = second_node  # 'a' is linked to 'b'.
second_node.next = third_node # 'b' is linked to 'c'.
llist
# %%
linked_list = LinkedList(['a', 'b', 'c', 'd'])
linked_list
for node in linked_list:
    print(node)
# %%
llist = LinkedList(['a', 'b', 'c'])
llist.add_after('b', 'e')
print(llist)
# %%
llist = LinkedList(['a', 'b', 'c'])
llist.remove_node('c')
llist.add_at_end('f')
print(llist)
#%%
llist1 = LinkedList(['a','b','c','d','e','f','g','h'])
llist2 = LinkedList(['l','m','n','o','p','e','f','g','h'])
print(size(llist1.head))
print(size(llist2.head))
intersecting_node = get_intersection(llist1.head, llist2.head)
print(intersecting_node)

# %%
# function to find the total number of nodes in a linked list
def size(head):
    nodes = 0
    while head:
        nodes += 1
        head = head.next
    return nodes

def get_intersection(headA, headB):
    lenA = size(headA)
    lenB = size(headB)
    print(f'len A is {lenA}')
    print(f'len B is {lenB}')

    while (lenA > lenB):
        headA = headA.next
        print('1st while loop {headA}')
        lenA -=1
    
    while (lenA < lenB):
        headB = headB.next
        print('2nd while loop')
        print(headB)
        lenB -=1
   
    while (headA.data != headB.data):
        headA = headA.next
        print(headA)
        headB = headB.next
        print(headB)
    
    return headA


# %%
# 1. Use stacks to implement a text editor. You are going to perform the following tasks:
# - Append(s): append a string s to the end of the file
# - delete(n): delete the last n characters from the string
# - print(n): print the last nth character from the string
# - undo(): undo the last operation corresponding to append or delete
# 2. The initial string is: `S = 'Hello World'`
# 3. operations = ['1 My name is Ivan', '3 10', '2 0', '4', '1 Ying', '3 15', '4']

class Text_editor:
    def __init__(self, text=None):
        self.text = text
        self.previous = text

    def append(self, s):
        self.previous = self.text
        self.text += " " + s

    def delete(self, n):
        self.previous = self.text
        self.text = self.text[:-n]

    def undo(self):
        self.text = self.previous

    def __repr__(self):
        return self.text

text = Text_editor("Hello World")
text.append("My name is Ivan")
print(text) 
text.undo()
print(text)
# %%
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.next = None
    def __repr__(self):
        return str(self.name)

class Animal_shelter():
    def __init__(self, animals=None):
        self.front = None
        self.rear = None 
        if animals:
            self.front = Animal(name=animals[0].name, type=animals[0].type)
            for i in range(0,len(animals)):
                animal = self.front 
            for i in range(1, len(animals)):
                animal.next = animals[i]
                animal = animal.next

    def __repr__(self):
        animal = self.front
        animals = []
        while animal is not None:
            animals.append(animal.name)
            animal = animal.next
        return  " Head/Front --> " + " ".join(animals) + " <-- Rear/Tail"
                
    def __iter__(self):
        animal = self.front
        while animal is not None:
            yield animal
            animal = animal.next

    def add(self, animal):
        if self.front is None:
            self.front = animal           
            return
        last = self.front
        while(last.next):
            last = last.next
        last.next = animal
        animal.next = None

    def is_empty(self):
        return self.front is None

    def remove(self, type=None):
        if self.is_empty():
            raise Exception("List is empty")
        animal = self.front
        if type is None or animal.type == type:
            self.front = animal.next
            return animal
        while animal.type != type and animal.next:
            previous_animal = animal 
            animal = animal.next
        if animal.type == type:
            previous_animal.next = animal.next      
            return animal


    def peek(self):
        if self.is_empty():
            return None
        return self.front


dog1 = Animal('alfie', 'dog')
dog2 = Animal('jess', 'dog')
cat1 = Animal('poppet', 'cat')
cat2 = Animal('archie', 'cat')
animals = [dog1,cat1,dog2,cat2]
shelter = Animal_shelter(animals)
print(shelter)
cat3 = Animal('tess', 'cat')
shelter.add(cat3)
print(shelter)
shelter.remove('dog')
print(shelter)
shelter.remove('cat')
print(shelter)
shelter.remove('dog')
print(shelter)


# %%

# %%
