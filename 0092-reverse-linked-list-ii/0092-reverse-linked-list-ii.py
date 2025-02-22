# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        resNode = curr = ListNode(0, head)
        i = 0

        def reverse(node, secondHalf):
            prev = secondHalf
            print(node)
            print(secondHalf)
            while node:
                temp = node.next
                node.next = prev
                prev = node 
                node = temp
            
            return prev
        
        while curr:
            if i == left - 1:
                second = secondCopy = curr.next

                j = i + 1
                while j < right:
                    secondCopy = secondCopy.next
                    j += 1
                third = secondCopy.next
                secondCopy.next = None
                curr.next = reverse(second, third)
                break

            curr = curr.next
            i += 1

        return resNode.next
