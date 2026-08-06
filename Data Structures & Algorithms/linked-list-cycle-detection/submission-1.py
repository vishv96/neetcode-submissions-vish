# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            node = head
            values = set()
            while node:
                if node in values:
                    return True
                values.add(node)
                node = node.next
        return False