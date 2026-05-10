# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        # to keep track of the latest node in our merged list
        tail = dummy

        while list1 != None and list2 != None:
            if list2.val >= list1.val:
                tail.next = list1
                list1 = list1.next

            elif list2.val < list1.val:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        

        return dummy.next
