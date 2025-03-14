# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcdAdj(self, a: int, b: int) -> int:
        while(b):
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return head

        curr = head
        while(curr and curr.next):
            temp = curr.next
            gcd = self.gcdAdj(curr.val, curr.next.val)
            middleNode = ListNode(gcd)
            middleNode.next = curr.next
            curr.next = middleNode
            curr = temp

        return head
        