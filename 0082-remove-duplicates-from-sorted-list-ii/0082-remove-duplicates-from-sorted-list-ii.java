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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0);
        ListNode prev = dummy;
        dummy.next = head;
        ListNode curr = dummy.next;

        while (curr != null) {
            if (curr.next != null && prev.next.val == curr.next.val) {
                ListNode temp = curr.next;
                while (temp.next != null && temp.next.val == prev.next.val) {
                    temp = temp.next;
                }
                curr = temp.next;
                prev.next = temp.next;
                continue;
            }
            prev = prev.next;
            curr = curr.next;
        }
        return dummy.next;
    }
}