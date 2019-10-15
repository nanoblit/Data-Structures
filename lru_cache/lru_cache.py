from doubly_linked_list import DoublyLinkedList

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.dll = DoublyLinkedList()
        self.storage = {}
        self.limit = limit
        self.length = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Try getting the value from the dll
        element = None
        node = self.dll.head
        for i in range(self.length - 1):
            if node.value.key == key:
                element = node
                break
            node = node.next
            
        # If found
        if element:
            # Move element to the end
            self.dll.move_to_end(element)
            # Return it
            return element.value.value
        # Return None
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Try finding the key in the dll
        found = None
        node = self.dll.head
        for i in range(self.length - 1):
            if node.value.key == key:
                found = node
                break
            node = node.next
        # If found
        if found:
            # Set its value to value
            found.value.value = value
            # Move it to the end
            self.dll.move_to_end(found)
        # Else
        else:
            # If length == limit
            if self.length == self.limit:
                # Remove the oldest (firs entry)
                self.dll.delete(self.dll.head)
            # Add entry at the end
            self.dll.add_to_tail(Node(key, value))
            # Length++
            self.length += 1
                
        pass
