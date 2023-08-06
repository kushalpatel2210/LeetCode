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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
       ListNode sumList = new ListNode(0);
       ListNode headNode = sumList;
        int carry = 0;

       while (l1 != null || l2 != null || carry != 0) {
        int l1Val = l1 != null ? l1.val : 0;
        int l2Val = l2 != null ? l2.val : 0;
        int sum = l1Val + l2Val + carry;
        int modulo = sum % 10;
        carry = sum /  10;
        headNode.next = new ListNode(modulo);

        if (l1 != null) {
            l1 = l1.next;
        }
        if (l2 != null) {
            l2 = l2.next;
        }

        headNode = headNode.next;
       }

       return sumList.next;
    }
}