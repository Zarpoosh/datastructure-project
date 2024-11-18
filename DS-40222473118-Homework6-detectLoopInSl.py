class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Adds a new node with the given value to the end of the list."""
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def create_loop(self, position):
        """
        Creates a loop in the linked list at the given position (0-based index).
        If position is invalid, no loop is created.
        """
        if not self.head:
            print("The list is empty, cannot create a loop.")
            return None

        loop_node = None
        current = self.head
        index = 0
        while current.next:
            if index == position:
                loop_node = current
            current = current.next
            index += 1

        if loop_node:
            current.next = loop_node
            print(f"Loop created at node with value: {loop_node.value}")
        else:
            print("Invalid position for creating a loop.")

    def detect_loop(self):
        """
        Detects if there is a loop in the linked list using Floyd's Cycle Detection Algorithm.
        Returns True if a loop is found, False otherwise.
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next          # Move slow pointer one step
            fast = fast.next.next     # Move fast pointer two steps
            if slow == fast:          # Loop detected
                return True
        return False

    def display(self):
        """Displays the linked list (only works if there's no loop)."""
        current = self.head
        visited = set()
        while current:
            if current in visited:  # To prevent infinite printing if there’s a loop
                print("... (loop detected, cannot display further)")
                return
            print(current.value, end=" -> ")
            visited.add(current)
            current = current.next
        print("None")


# Main function to take user inputs and test the linked list
def main():
    linked_list = LinkedList()
    
    # Take inputs for the linked list
    print("Enter values for the linked list nodes (type 'done' to finish):")
    while True:
        value = input("Enter node value: ")
        if value.lower() == 'done':
            break
        linked_list.append(int(value))

    # Display the linked list
    print("Linked list created:")
    linked_list.display()

    # Take input to create a loop
    loop_position = int(input("Enter the position (0-based index) to create a loop, or -1 to skip: "))
    if loop_position >= 0:
        linked_list.create_loop(loop_position)

    # Detect if there's a loop
    if linked_list.detect_loop():
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")


if __name__ == "__main__":
    main()
