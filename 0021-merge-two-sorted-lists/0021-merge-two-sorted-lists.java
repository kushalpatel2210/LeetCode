/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode mergedList = new ListNode(0);
        ListNode headNode = mergedList;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                headNode.next = list1;
                list1 = list1.next;
            } else {
                headNode.next = list2;
                list2 = list2.next;
            }
            headNode = headNode.next;
        }

        if (list1 != null) {
            headNode.next = list1;
        }

        if (list2 != null) {
            headNode.next = list2;
        }

        return mergedList.next;
    }
} 