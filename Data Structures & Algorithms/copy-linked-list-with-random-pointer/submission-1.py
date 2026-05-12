"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        node_hash = {}

        ptr1 = head
        deep_copy = Node(ptr1.val)
        deep_copy_head = deep_copy
        curr_copy = deep_copy_head

        while ptr1.next != None:
            node_hash[ptr1] = deep_copy
            ptr1 = ptr1.next
            deep_copy.next = Node(ptr1.val)
            deep_copy = deep_copy.next

        node_hash[ptr1] = deep_copy


        ptr2 = head
        while ptr2:
            deep_copy_head.val = ptr2.val
            if ptr2.random == None:
                deep_copy_head.random = None
            else:
                deep_copy_head.random = node_hash[ptr2.random]
            ptr2 = ptr2.next
            deep_copy_head = deep_copy_head.next

        return curr_copy
            

