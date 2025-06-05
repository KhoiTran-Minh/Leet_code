class UnionFind:
    def __init__(self):
        self.parent = {chr(ord('a') + i): chr(ord('a') + i) for i in range(26)}

    def find(self, char):
        if self.parent[char] == char:
            return char
        self.parent[char] = self.find(self.parent[char])
        return self.parent[char]

    def union(self, char1, char2):
        root1 = self.find(char1)
        root2 = self.find(char2)

        if root1 != root2:
            if root1 < root2:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        uf = UnionFind()

        for i in range(len(s1)):
            uf.union(s1[i], s2[i])

        result = []
        for char in baseStr:
            result.append(uf.find(char)) 
        
        return "".join(result)
        