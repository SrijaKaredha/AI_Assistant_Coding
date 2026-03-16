Task1:
class Stack:
    """
    A simple Stack data structure implementation using a Python list.
    Supports push, pop, peek, and is_empty operations.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The element to be added to the stack.
        """
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The element at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Return the top item from the stack without removing it.

        Returns:
            The element at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0


# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.peek())  # Output: 30
    print("Popped element:", stack.pop())  # Output: 30
    print("Is stack empty?", stack.is_empty())  # Output: False
    print("Popped element:", stack.pop())  # Output: 20
    print("Popped element:", stack.pop())  # Output: 10
    print("Is stack empty?", stack.is_empty())  # Output: True


Task 2:
class Queue:
    """
    A simple Queue implementation using a Python list.
    Follows the FIFO (First-In-First-Out) principle.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        :param item: Item to be added.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        :return: The item at the front of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        :return: The item at the front of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        """
        Return the number of items in the queue.
        :return: Size of the queue.
        """
        return len(self.items)

    def is_empty(self):
        """
        Check if the queue is empty.
        :return: True if empty, False otherwise.
        """
        return len(self.items) == 0

# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue size:", q.size())      # Output: 3
    print("Front item:", q.peek())      # Output: 10
    print("Dequeued:", q.dequeue())     # Output: 10
    print("Queue size after dequeue:", q.size())  # Output: 2

Task 3:
class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data: The value stored in the node.
        next: Reference to the next node in the list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Implements a singly linked list.

    Methods:
        insert(data): Inserts a new node with the given data at the end of the list.
        display(): Prints the elements of the list.
    """
    def __init__(self):
        self.head = None

    def insert(self, data):
        """
        Inserts a new node with the specified data at the end of the list.

        Args:
            data: The value to be inserted.
        """
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, set head to new node
            self.head = new_node
        else:
            # Traverse to the end and insert the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """
        Prints the elements of the linked list in order.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Linked List:", " -> ".join(elements))


# Example usage
if __name__ == "__main__":
    # Create a linked list
    ll = LinkedList()
    # Insert elements
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    # Display the list
    ll.display()

Task 4:
class Node:
    """
    Represents a node in the Binary Search Tree.
    Each node contains a value and references to left and right child nodes.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Implements a Binary Search Tree (BST) with recursive insert and in-order traversal methods.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the BST.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursively inserts a value starting from the given node.
        """
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # If value == node.value, do not insert duplicates
        return node

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the BST and returns a list of values.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """
        Recursively traverses the BST in-order and appends values to result.
        """
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    values_to_insert = [7, 3, 9, 1, 5, 8, 10]
    for value in values_to_insert:
        bst.insert(value)

    print("In-order traversal of BST:", bst.inorder_traversal())
    # Output: In-order traversal of BST: [1, 3, 5, 7, 8, 9, 10]

Task 5:

class HashTable:
    """
    Hash Table implementation using chaining for collision handling.
    Each bucket is a list of key-value pairs.
    """

    def __init__(self, size=10):
        """
        Initialize the hash table with a given size.
        :param size: Number of buckets in the hash table.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Compute the hash value for a given key.
        :param key: Key to hash.
        :return: Index of the bucket.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        :param key: Key to insert.
        :param value: Value to associate with the key.
        """
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        """
        Search for a key in the hash table and return its value.
        :param key: Key to search for.
        :return: Value associated with the key, or None if not found.
        """
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        :param key: Key to delete.
        :return: True if deleted, False if key not found.
        """
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        """
        String representation of the hash table for debugging.
        """
        return str(self.table)


# Example usage
if __name__ == "__main__":
    ht = HashTable(size=5)
    # Insert key-value pairs
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)
    ht.insert("grape", 40)

    print("Hash Table after insertions:")
    print(ht)

    # Search for keys
    print("Search for 'banana':", ht.search("banana"))
    print("Search for 'cherry':", ht.search("cherry"))

    # Delete a key
    print("Delete 'orange':", ht.delete("orange"))
    print("Hash Table after deletion:")
    print(ht)

Task 6:
lass Graph:
    """
    Graph implementation using adjacency list representation.
    """

    def __init__(self):
        """
        Initializes an empty graph with an adjacency list.
        """
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Args:
            vertex: The vertex to be added.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Adds an edge between vertex1 and vertex2.

        Args:
            vertex1: The starting vertex.
            vertex2: The ending vertex.
        """
        # Ensure both vertices exist
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        # Add the edge (undirected graph)
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def display_graph(self):
        """
        Displays the adjacency list of the graph.
        """
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex}: {neighbors}")


# Example usage
if __name__ == "__main__":
    # Create a new graph
    graph = Graph()

    # Add vertices
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')

    # Add edges
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')

    # Display the graph
    graph.display_graph()

    Task 7:
    import heapq

class PriorityQueue:
    """
    A Priority Queue implementation using the heapq module.
    Elements with higher priority are dequeued first.
    """

    def __init__(self):
        """
        Initialize an empty priority queue.
        """
        self._heap = []
        self._counter = 0  # To handle items with same priority

    def enqueue(self, item, priority):
        """
        Add an item to the queue with the given priority.
        Higher priority values are dequeued first.

        Args:
            item: The item to be added.
            priority: The priority of the item (higher value = higher priority).
        """
        # Negate priority because heapq is a min-heap
        heapq.heappush(self._heap, (-priority, self._counter, item))
        self._counter += 1

    def dequeue(self):
        """
        Remove and return the item with the highest priority.

        Returns:
            The item with the highest priority.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self._heap:
            raise IndexError("dequeue from empty priority queue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def display(self):
        """
        Display the contents of the priority queue in priority order.
        """
        # Create a sorted list for display purposes
        sorted_items = sorted(self._heap, reverse=True)
        print("Priority Queue contents (highest priority first):")
        for priority, _, item in sorted_items:
            print(f"Item: {item}, Priority: {-priority}")

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Task A", priority=2)
    pq.enqueue("Task B", priority=5)
    pq.enqueue("Task C", priority=3)
    pq.display()

    print("\nDequeued:", pq.dequeue())
    pq.display()

    Task 8:
    from collections import deque

class Deque:
    """
    A double-ended queue (Deque) implementation using collections.deque.
    Supports insertion and removal from both ends.
    """

    def __init__(self):
        """Initialize an empty deque."""
        self._deque = deque()

    def insert_front(self, item):
        """
        Insert an item at the front of the deque.
        :param item: Item to be inserted.
        """
        self._deque.appendleft(item)

    def insert_rear(self, item):
        """
        Insert an item at the rear of the deque.
        :param item: Item to be inserted.
        """
        self._deque.append(item)

    def remove_front(self):
        """
        Remove and return the item from the front of the deque.
        :return: Item removed from the front.
        :raises IndexError: If the deque is empty.
        """
        if not self._deque:
            raise IndexError("remove_front(): Deque is empty")
        return self._deque.popleft()

    def remove_rear(self):
        """
        Remove and return the item from the rear of the deque.
        :return: Item removed from the rear.
        :raises IndexError: If the deque is empty.
        """
        if not self._deque:
            raise IndexError("remove_rear(): Deque is empty")
        return self._deque.pop()

    def __str__(self):
        """Return string representation of the deque."""
        return f"Deque({list(self._deque)})"


# Example usage
if __name__ == "__main__":
    dq = Deque()
    dq.insert_front(10)
    dq.insert_rear(20)
    dq.insert_front(5)
    print("After insertions:", dq)

    front = dq.remove_front()
    print("Removed from front:", front)
    rear = dq.remove_rear()
    print("Removed from rear:", rear)
    print("Final deque:", dq)

    Task 9:
    from collections import deque

# Feature → Data Structure → Justification

# | Feature                   | Data Structure   | Justification                                                                 |
# |---------------------------|------------------|-------------------------------------------------------------------------------|
# | Student Attendance Tracking| Hash Table       | Efficient lookup and update of attendance records by student ID.              |
# | Event Registration System  | Queue            | Registrations are processed in order; a queue ensures FIFO handling.          |
# | Library Book Borrowing     | Hash Table       | Quick access to borrowing records by book or user; supports fast updates.     |
# | Bus Scheduling System      | Priority Queue   | Buses can be scheduled based on priority (e.g., departure time or urgency).   |
# | Cafeteria Order Queue      | Queue            | Orders are served in the order they are placed; queue ensures fairness.       |

# Below is an implementation of the Event Registration System using a Queue.


class EventRegistrationQueue:
    """
    A queue-based event registration system.
    Registrations are processed in the order they are received (FIFO).
    """
    def __init__(self):
        self.queue = deque()

    def register(self, participant_name):
        """
        Add a participant to the registration queue.
        """
        self.queue.append(participant_name)
        print(f"{participant_name} registered.")

    def process_registration(self):
        """
        Process the next registration in the queue.
        """
        if self.queue:
            participant = self.queue.popleft()
            print(f"Processed registration for: {participant}")
            return participant
        else:
            print("No registrations to process.")
            return None

    def show_queue(self):
        """
        Display the current registration queue.
        """
        print("Current registration queue:", list(self.queue))

# Example usage:
if __name__ == "__main__":
    event_queue = EventRegistrationQueue()
    event_queue.register("Alice")
    event_queue.register("Bob")
    event_queue.register("Charlie")
    event_queue.show_queue()
    event_queue.process_registration()
    event_queue.show_queue()

    Task 10:
    from collections import deque

# Feature → Data Structure → Justification Table

| Feature                     | Data Structure      | Justification                                                                                  |
|-----------------------------|--------------------|-----------------------------------------------------------------------------------------------|
| Shopping Cart Management    | Hash Table         | Hash tables allow fast addition, removal, and lookup of products in the cart by product ID.    |
| Order Processing System     | Queue              | Orders are processed in the order they arrive (FIFO), making queue ideal for this workflow.    |
| Top-Selling Products Tracker| Priority Queue     | Priority queue efficiently keeps track of products with highest sales for quick retrieval.     |
| Product Search Engine       | Binary Search Tree | BST enables efficient searching, insertion, and deletion of products based on searchable keys. |
| Delivery Route Planning     | Graph              | Graphs model locations and routes, enabling optimal pathfinding for delivery logistics.        |

# Implementation: Order Processing System using Queue


class OrderProcessingSystem:
    """
    A simple order processing system using a queue.
    Orders are processed in the order they are received (FIFO).
    """
    def __init__(self):
        self.order_queue = deque()

    def add_order(self, order_id):
        """
        Add a new order to the processing queue.
        :param order_id: Unique identifier for the order.
        """
        self.order_queue.append(order_id)
        print(f"Order {order_id} added to queue.")

    def process_order(self):
        """
        Process the next order in the queue.
        :return: The processed order ID or None if queue is empty.
        """
        if self.order_queue:
            order_id = self.order_queue.popleft()
            print(f"Order {order_id} processed.")
            return order_id
        else:
            print("No orders to process.")
            return None

# Example usage
if __name__ == "__main__":
    ops = OrderProcessingSystem()
    ops.add_order("ORD001")
    ops.add_order("ORD002")
    ops.process_order()
    ops.process_order()
    ops.process_order()
