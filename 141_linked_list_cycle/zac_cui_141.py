#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-11 12:44:44
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        _curr, _next = head, head.next
        while _next and _next.next:
            if _curr == _next:
                return True
            _curr = _curr.next
            _next = _next.next.next
        return False
            