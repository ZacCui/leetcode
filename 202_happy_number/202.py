class Solution:
    def isHappy(self, n: 'int') -> 'bool':
        dic = {}
        while n not in dic:
            dic[n] = 1
            n = sum([int(i)**2 for i in str(n)])
            if n == 1:
                return True
        return False