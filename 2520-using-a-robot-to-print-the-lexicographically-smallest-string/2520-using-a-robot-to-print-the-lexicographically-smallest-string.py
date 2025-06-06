class Solution(object):
    def robotWithString(self, s):
        n = len(s)
        if n == 0:
            return ""

        min_char_suffix = [''] * n
        min_char_suffix[n - 1] = s[n - 1]
        for i in range(n - 2, -1, -1):
            min_char_suffix[i] = min(s[i], min_char_suffix[i + 1])

        paper = []  
        t = []      

        for i in range(n):
            while t and t[-1] <= min_char_suffix[i]:
                paper.append(t.pop())

            t.append(s[i])
        while t:
            paper.append(t.pop())
            
        return "".join(paper)
        