"""
Stack Data Structure Implementation
A simple stack implementation using a Python list with push, pop, peek, and is_empty methods.
"""


class Stack:
    """A stack data structure that follows LIFO (Last In First Out) principle."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The element to be added to the stack.
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top element of the stack, or None if stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """
        View the top item without removing it.
        
        Returns:
            The top element of the stack, or None if stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0


# Test cases
if __name__ == "__main__":
    stack = Stack()
    
    # Test is_empty on new stack
    print(f"Is empty: {stack.is_empty()}")  # Output: True
    
    # Test push
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Is empty after push: {stack.is_empty()}")  # Output: False
    
    # Test peek
    print(f"Peek: {stack.peek()}")  # Output: 30
    
    # Test pop
    print(f"Pop: {stack.pop()}")  # Output: 30
    print(f"Pop: {stack.pop()}")  # Output: 20
    
    # Test peek after pop
    print(f"Peek: {stack.peek()}")  # Output: 10
    
    # Pop remaining item
    stack.pop()
    print(f"Is empty after popping all: {stack.is_empty()}")  # Output: True