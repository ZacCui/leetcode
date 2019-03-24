#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-03-24 16:11:57
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = ('(' , '{' , '[')
        mapping = {')' : '(', '}':'{', ']' : '['}
        for c in s:
            if c in dic:
                stack.append(c)
            elif c in mapping:
                if not len(stack) or mapping[c] != stack.pop(-1):
                    return False
                
        return not len(stack)
            
            
        