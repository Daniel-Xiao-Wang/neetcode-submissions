# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        first = ListNode()
        res = first

        if cur1 is None:
            return cur2
        elif cur2 is None:
            return cur1
        
        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                res.next = cur1
                res = res.next
                cur1 = cur1.next
            else:
                res.next = cur2
                res = res.next
                cur2 = cur2.next
            print(res.val)
        
        if cur1 is None:
                res.next = cur2
        else:
                res.next = cur1
    
        return first.next