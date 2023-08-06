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
    public ListNode middleNode(ListNode head) {
        int size = 0;
        int iterator = 0; 
        ListNode curr = head;
        ListNode middle = null; 

        while (curr != null) {
            size++;
            curr = curr.next;
        }

        int median = size / 2;

        while (head != null) {
            if (iterator == median) {
                middle = head;
                break;
            }
            iterator++;
            head = head.next;
        }

        return middle;
    }
}