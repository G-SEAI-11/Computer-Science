class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        # self.tail = None

    def append(self, value):  # O(n)
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:  # Traversal / Traversierung
                current_node = current_node.next

            current_node.next = new_node

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def pop(self):  # O(n)
        if not self.head:
            return None

        if not self.head.next:
            val = self.head.value
            self.head = None
            return val

        current_node = self.head
        prev_node = self.head

        while current_node.next:
            prev_node = current_node
            current_node = current_node.next

        val = current_node.value
        prev_node.next = None
        return val

    def remove(self, value):
        pass

    def __str__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(f"[{ curr.value }]")
            curr = curr.next

        return " -> ".join(nodes) + " -> None"


my_linked_list = LinkedList()

my_linked_list.append(42)
my_linked_list.append("test")
my_linked_list.append(False)
my_linked_list.append(123)
my_linked_list.append(1.23)

print(my_linked_list)


last = my_linked_list.pop()
print(my_linked_list)
print(last)


# my_py_list = []

# my_py_list.append(42)

# [1, 2, 3] + [6, 7, 8]

# 42.plus(52)


# 42 + 54

# "Guten, " + "morgen"
