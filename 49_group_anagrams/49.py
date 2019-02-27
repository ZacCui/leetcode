#!/usr/local/bin/python3

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        index = 0
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in dic:
                dic[sorted_s] = index
                res.append([s])
                index += 1     
            else:
                res[dic[sorted_s]].append(s)
        return res