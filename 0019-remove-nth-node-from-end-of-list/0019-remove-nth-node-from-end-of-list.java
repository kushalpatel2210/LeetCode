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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode newNode = new ListNode(0);
        ListNode headNode = head;
        newNode.next = head;
        ListNode newNodeHead = newNode;
        int size = 0;
        int counter = 0;

        while (headNode != null) {
            size++;
            headNode = headNode.next;
        }

        while (newNodeHead != null) {
            if (counter == size - n) {
                ListNode nextNode = newNodeHead.next != null ? newNodeHead.next.next : null;
                newNodeHead.next = nextNode;
                break;
            }
            counter++;
            newNodeHead = newNodeHead.next;
        }
        return newNode.next;
    }
}