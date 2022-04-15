# LeetCode 707.
# https://leetcode.com/problems/design-linked-list/

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# =========================================================================
# Singly Linked List Solution

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
    
    # time: O(index), space: O(1)
    def get(self, index: int) -> int:
        if index >= self.size or index < 0 or self.head is None:
            return -1
  
        target = self.head
        for _ in range(index):
            target = target.next
        return target.val
        
    # time: O(1), space: O(1)
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        
        self.size += 1 
    
    # time: O(n), space: O(1)
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            target = self.head
            while target.next is not None:
                target = target.next
            target.next = node
        self.size += 1
    
     # time: O(index), space: O(1)
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        
        if index == 0:
            self.addAtHead(val)
        else:
            node = Node(val)
            target = self.head
            for _ in range(index - 1):
                target = target.next
                
            node.next = target.next
            target.next = node
            self.size += 1
    
     # time: O(index), space: O(1)
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            target = node.next
            node.next = target.next
            target.next = None

        self.size -= 1

# =========================================================================
# Doubly Linked List Solution

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    # time: O(index), space: O(1)
    def get(self, index: int) -> int:
        if index < 0 or self.head is None:
            return -1
  
        target = self.head
        currIndex = 0
        while target is not None and currIndex != index:
            target = target.next
            currIndex += 1
        return target.val if target is not None else -1
        
    # time: O(1), space: O(1)
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    # time: O(1), space: O(1)
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is None:
            self.tail = self.head = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    
     # time: O(index), space: O(1)
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)

        if index < 0 or self.head is None:
            return

        else:
            node = Node(val)
            target = self.head
            currIndex = 0
            while target.next is not None and currIndex != index - 1:
                target = target.next
                currIndex += 1
                
            if target.next is None:
                if currIndex != index - 1:
                    return
                target.next = node
                node.prev = target
                self.tail = node
            else:
                node.prev = target
                node.next = target.next
                target.next.prev = node
                target.next = node

     # time: O(index), space: O(1)
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.head is None:
            return
        
        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None 
        else:
            node = self.head
            currIndex = 0
            while node.next is not None and currIndex != index:
                node = node.next
                currIndex += 1
                
            if node.next is None:
                if currIndex != index:
                    return
                self.tail = node.prev
                self.tail.next = None
            else:
                node.next.prev = node.prev
                node.prev.next = node.next

# =========================================================================

# AlgoExpert Linked List No.2 -> Doubly Linked List 
class Node:
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None
		
class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	
	# time: O(1), space: O(1)
	def setHead(self, node):
		if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)
	
	# time: O(1), space: O(1)
	def setTail(self, node):
		if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail, node)
	
	# time: O(1), space: O(1)
	def insertBefore(self, target, node):
		if node == self.head and node == self.tail:
			return
		
		self.remove(node) # need considering head, tail, existing, stand-alone
		preNode = target.prev
		node.next = target
		node.prev = preNode
		target.prev = node
		if preNode is not None:
			preNode.next = node
		else:
			self.head = node
		
	# time: O(1), space: O(1)
	def insertAfter(self, target, node):
		if node == self.head and node == self.tail:
			return
		
		self.remove(node)
		nextNode = target.next
		node.next = nextNode
		node.prev = target
		target.next = node
		if nextNode is not None:
			nextNode.prev = node
		else:
			self.tail = node
	
	# time: O(p), space: O(1)
	def insertAtPosition(self, position, node):
		# if position == 1:
		# 	self.setHead(node)
		# 	return
		index = 1
		target = self.head
		while target is not None and index != position:
			target = target.next
			index += 1
		if target is not None:
			self.insertBefore(target, node)
		else:
			self.setTail(node)
	
	# time: O(n), space: O(1)
	def removeNodesWithValue(self, value):
		node = self.head
		while node is not None:
			target = node
			node = node.next
			if target.value == value:
				self.remove(target)
				
	# time: O(1), space: O(1)
	def remove(self, node):
		if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None
		
	# time: O(n), space: O(1)
	def containsNodeWithValue(self, value):
		target = self.head
		while target is not None and target.value != value:
			target = target.next
		return target is not None

