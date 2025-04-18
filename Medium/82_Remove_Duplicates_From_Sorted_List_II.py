# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(head is None or head.next is None):
            return head

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while(curr):
            isDup = False
            while(curr.next and curr.val == curr.next.val):
                isDup = True
                curr = curr.next

            if(isDup):
                prev.next = curr.next
            else:
                prev = prev.next

            curr = curr.next

        return dummy.next