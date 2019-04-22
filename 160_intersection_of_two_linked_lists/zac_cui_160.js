/*
	Author: Zac Cui
	Created Date: 2019-04-22 20:16:03
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    if (!headA && !headB) return null;
    let set = new Set(); 
    let currA = headA;
    let currB = headB;
    while (currA != null) {
        set.add(currA)
        currA = currA.next;
    } 
    
    while (currB != null) {
        if (set.has(currB)){
            return currB;
        }
        currB = currB.next;
    } 
    
    return null
};