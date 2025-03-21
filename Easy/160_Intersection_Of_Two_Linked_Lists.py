# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if(headA is None or headB is None):
            return None

        countA = 0
        countB = 0

        tempA = headA
        tempB = headB

        while(tempA):
            countA += 1
            tempA = tempA.next

        while(tempB):
            countB += 1
            tempB = tempB.next

        tempA = headA
        tempB = headB

        diff = abs(countA - countB)

        if(countA > countB):
            while(diff > 0):
                tempA = tempA.next
                diff -= 1
        else:
            while(diff > 0):
                tempB = tempB.next
                diff -= 1
        
        while( tempA is not None):
            if(tempA == tempB):
                return tempA
            tempA = tempA.next
            tempB = tempB.next

        return None