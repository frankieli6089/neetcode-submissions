# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        count = 0
        count2 = 0
        while l1:
            num1 += l1.val * (pow(10, count))
            l1 = l1.next
            count += 1 
        while l2:
            num2 += l2.val * (pow(10, count2))
            l2 = l2.next
            count2 += 1 
    
        total = num1 + num2
       
        new = ListNode()
        new_head = new
        while total >= 10:
            new_head.val = (total % 10)
            total = total // 10
            new_head.next = ListNode()
            new_head = new_head.next
        
        new_head.val = total
        new_head.next = None

        return new

