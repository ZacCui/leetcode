#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-10 11:29:16
'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not len(s): return True
        s = re.sub("\W*|\s*", '', s).lower()
        return s == ''.join(reversed(s))