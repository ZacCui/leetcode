/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(1);
        ListNode first = dummy;
        ListNode second = dummy;
        dummy.next = head;
        for (int i = 0; i != n + 1 ; ++i){
            first = first.next;
        }
        while (first != null){
            first = first.next;
            second = second.next;
        }
        
        second.next = second.next.next;
        return dummy.next;
    }
}