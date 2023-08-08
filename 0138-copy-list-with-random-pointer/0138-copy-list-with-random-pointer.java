/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node> copyMap = new LinkedHashMap<>();
        Node headNode = head;
        Node headNodeCopy = head;
        Node deepCopy = new Node(0);
        Node deepCopyHeadNode = deepCopy;

        while (headNode != null) {
            copyMap.put(headNode, new Node(headNode.val));
            headNode = headNode.next;
        }

        for (Map.Entry<Node, Node> entry: copyMap.entrySet()) {
            Node newNode = entry.getValue();
            newNode.next = copyMap.get(headNodeCopy.next);
            newNode.random = copyMap.get(headNodeCopy.random);
            deepCopyHeadNode.next = newNode;
            headNodeCopy = headNodeCopy.next;
            deepCopyHeadNode = deepCopyHeadNode.next;
        }

        return deepCopy.next;
    }
}