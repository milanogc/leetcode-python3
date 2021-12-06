# https://leetcode.com/problems/middle-of-the-linked-list

from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            node1 = self
            node2 = other

            while node1 and node2:
                if node1.val != node2.val:
                    return False
                
                node1 = node1.next
                node2 = node2.next

            if (node1 is None) != (node2 is None):
                return False
            
            return True
        else:
            return False

    def __repr__(self) -> str:
        values = []
        node = self

        while node:
            values.append(node.val)
            node = node.next
        
        return str(values)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

# Tests

def createLinkedList(data: List[int]) -> Optional[ListNode]:
    if not data or len(data) == 0:
        return None

    head = node = ListNode()

    for v in data:
        node.val = v
        node.next = ListNode()
        node, last = node.next, node

    last.next = None
    return head

assert Solution().middleNode(createLinkedList([1,2,3,4,5])) == createLinkedList([3,4,5])
assert Solution().middleNode(createLinkedList([1,2,3,4,5,6])) == createLinkedList([4,5,6])
assert Solution().middleNode(createLinkedList([1])) == createLinkedList([1])