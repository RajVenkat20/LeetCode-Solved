# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if(head is None or head.next is None):
            return head
        cnt = 1
        curr = head

        while(curr.next):
            curr = curr.next
            cnt += 1
        
        k = k % cnt
        if(k == 0):
            return head

        temp = head
        for i in range(cnt - k - 1):
            temp = temp.next
        
        newHead = temp.next
        temp.next = None
        curr.next = head
        
        return newHead