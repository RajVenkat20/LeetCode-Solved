# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head is None or head.next == None):
            return False
        
        temp = head

        nodes = set()

        while(temp is not None):
            if(temp in nodes):
                return True
            
            nodes.add(temp)
            temp=temp.next

        return False