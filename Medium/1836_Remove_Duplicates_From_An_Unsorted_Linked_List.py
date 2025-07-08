# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if(head is None):
            return head

        hm = {}
        dummy = ListNode(-1, head)
        temp = dummy.next
        prev = dummy

        curr = head
        while(curr):
            hm[curr.val] = hm.get(curr.val, 0) + 1
            curr = curr.next

        while(temp):
            if(hm[temp.val] > 1):
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next

        return dummy.next