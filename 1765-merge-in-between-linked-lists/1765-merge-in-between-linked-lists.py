# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node1 = ListNode(0, list1)
        node2 = ListNode(0, list2)
        node2 = node2.next
        lastNode = ListNode()
        i = 1

        while node2:
            lastNode.next = node2
            node2 = node2.next

        while list1:
            # print(i)
            if i == a:
                curr = list1
                # print(curr)

                for _ in range(b - a + 2):
                    list1 = list1.next
                # print(list1)
                curr.next = list2
                lastNode.next.next = list1
                return node1.next

            list1 = list1.next
            i += 1

        return list1
