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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummyNode = new ListNode(0);
        dummyNode.next = head;
        ListNode leftNode = dummyNode;
        ListNode rightNode = dummyNode;
        ListNode lastNodeofReversedList = dummyNode;
        ListNode curr = dummyNode;
        int counter = 0;

        if (left == right) {
            return head;
        }

        while (curr != null) {
            if (counter == left - 1) {
                leftNode = curr;
            }

            ListNode prev = leftNode;
            while (counter >= left && counter <= right ) {
                if (counter == left) {
                    lastNodeofReversedList = curr;
                }

                if (counter == right) {
                    rightNode = curr.next;
                }
                ListNode temp = curr.next;
                curr.next = prev;
                prev = curr;
                if (counter == right) {
                    break;
                }
                curr = temp;
                counter++;
            }

            if (counter == right) {
                lastNodeofReversedList.next = rightNode;
                leftNode.next = prev;
            }
            counter++;
            curr = curr.next;
        }

        return dummyNode.next;
    }
}