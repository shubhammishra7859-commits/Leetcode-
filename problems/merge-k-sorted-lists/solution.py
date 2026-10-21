# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        # Min-heap to store tuples of (node.val, index, node)
        heap = []
        for i, l in enumerate(lists):
            if l:
                # We use 'i' as a tie-breaker so Python doesn't compare ListNode objects directly
                heapq.heappush(heap, (l.val, i, l))
                
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # If there is a next node in the same linked list, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next