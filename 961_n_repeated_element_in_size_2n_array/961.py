class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        dic = {}
        for val in A:
            if val in dic:
                return val
            dic[val] = 1