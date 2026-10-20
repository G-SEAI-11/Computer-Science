class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def dequeue(self):  # O(1)
        if not self.head:
            return None

        dequeued_val = self.head.value
        self.head = self.head.next

        if not self.head:
            self.tail = None

        self.length -= 1
        return dequeued_val

    def __str__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(f"[{curr.value}]")
            curr = curr.next
        return "(Head) " + " <- ".join(nodes) + " (Tail)"
