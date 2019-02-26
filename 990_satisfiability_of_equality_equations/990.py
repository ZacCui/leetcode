#!/usr/local/bin/python3

class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        g = [[] for i in range(26)]
        for e in equations:
            if e[1] == '=':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                g[x].append(y)
                g[y].append(x)
        
        color = [None] * 26
        tag = 0
        
        for i in range(26):
            if color[i] is None:
                tag += 1
                stack = [i]
                while len(stack):
                    node = stack.pop()
                    for n in g[node]:
                        if color[n] is None:
                            color[n] = tag
                            stack.append(n)

        for e in equations:
            if e[1] == '!':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                if x == y: return False
                if color[x] is not None and color[x] == color[y]:
                    return False
        return True
                