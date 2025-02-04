# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            if(l1 is None and l2 is not None):
                return l2
            elif( l2 is None and l1 is not None):
                return l1

            first = l1
            second = l2
            carry = 0

            dummy = ListNode(-1)
            temp = dummy

            while(first and second):
                val = first.val + second.val + carry
                temp.next = ListNode(val % 10)
                carry = val // 10

                if(first.next is None and second.next is None and carry != 0):
                    temp = temp.next
                    temp.next = ListNode(1)

                temp = temp.next
                if(first):
                    first = first.next
                if(second):
                    second = second.next

            while(first):
                val = first.val + carry
                temp.next = ListNode(val % 10)
                carry = val // 10

                if(first.next is None and carry != 0):
                    temp = temp.next
                    temp.next = ListNode(1)
                    
                first = first.next
                temp = temp.next

            while(second):
                val = second.val + carry
                temp.next = ListNode(val % 10)
                carry = val // 10

                if(second.next is None and carry != 0):
                    temp = temp.next
                    temp.next = ListNode(1)

                second = second.next
                temp = temp.next

            dummy = dummy.next

            return dummy