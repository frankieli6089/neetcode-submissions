# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        node_count = 0
        ptr1 = head
        while ptr1:
            ptr1 = ptr1.next
            node_count +=1 
        ptr2 = head

        curr_node_count = 0
        while ptr2:
            if ptr2.next == None and curr_node_count == (node_count - n):
                ptr2 = None
                return ptr2
            elif curr_node_count == (node_count - n) and curr_node_count == 0:
                return ptr2.next
            elif curr_node_count + 1 == (node_count - n):
                tmp = ptr2
                ptr2.next = tmp.next.next
                return dummy

            ptr2 = ptr2.next
            curr_node_count += 1
        
