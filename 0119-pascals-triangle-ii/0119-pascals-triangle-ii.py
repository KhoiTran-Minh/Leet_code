class Solution(object):
    def getRow(self, rowIndex):
        pascal_triangle = []
        for i in range(0,rowIndex+1):
            pascal_triangle.append([1] * (i + 1))
        for i in range(2,rowIndex +1):
            for j in range(1,i):
                pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
        return pascal_triangle[rowIndex]

        