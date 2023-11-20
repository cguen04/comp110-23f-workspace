"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        return self.data

    def tail(self) -> Node | None:
        if self.next is None:
            return None
        else:
            return str(self.next)

    def last(self) -> int:
        if self.next == None:
            return self.data
        x: list = [self.data, self.next,]
        return x[len(x)]
