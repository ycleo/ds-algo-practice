
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
	prevNode, currNode = None, head
	
	while currNode != None:
		nextNode = currNode.next
		currNode.next = prevNode
		prevNode = currNode
		currNode = nextNode
	return prevNode
# time: O(n)
# space: O(1)