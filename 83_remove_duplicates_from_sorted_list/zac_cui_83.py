#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-06 16:00:50
'''

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: return head
        prev, curr = head, head.next
        while curr != None:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return head