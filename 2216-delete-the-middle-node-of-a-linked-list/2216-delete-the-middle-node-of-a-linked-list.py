# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copyOfHead = head
        length = 0

        while copyOfHead:
            length += 1
            copyOfHead = copyOfHead.next
        
        middle = length // 2
        curr = ListNode()
        curr.next = head
        i = 0

        if middle == 0:
            return None

        while head:
            if i == middle - 1:
                head.next = head.next.next
                break
            else:
                head = head.next
            i += 1

        return curr.next 
        