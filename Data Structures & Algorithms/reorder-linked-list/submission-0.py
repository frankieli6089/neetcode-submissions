# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast_ptr = head
        slow_ptr = head

        while fast_ptr.next != None:
            fast_ptr = fast_ptr.next
            if fast_ptr.next == None:
                break
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next



        l1 = head
        l2 = slow_ptr.next
        slow_ptr.next = None

        prev = None
        curr = l2

        while curr:
            next_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = next_ptr

        while prev:
            tmp1 = l1.next
            tmp2 = prev.next

            l1.next = prev
            prev.next = tmp1

            l1 = tmp1
            prev = tmp2
        
