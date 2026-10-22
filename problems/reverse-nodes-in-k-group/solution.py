# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1. Find the k-th node from the current group's previous node
            kth = self._get_kth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next

            # 2. Reverse the k nodes
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 3. Connect the reversed group with the rest of the list
            temp = group_prev.next  # This will become the tail of the reversed group
            group_prev.next = kth
            group_prev = temp

        return dummy.next

    def _get_kth(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr