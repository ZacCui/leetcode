#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-03-24 18:32:26
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return l1
        if l2 == None:
            return l1
        if l1 == None:
            return l2
        curr1, curr2 = l1, l2
        head = l1 if l1.val <= l2.val else l2
        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                while curr1 != None and curr1.val <= curr2.val:
                    prev1 = curr1
                    curr1 = curr1.next
                prev1.next = curr2
            else:
                while curr2 != None and curr1.val > curr2.val:
                    prev2 = curr2
                    curr2 = curr2.next
                prev2.next = curr1
                
        return head     