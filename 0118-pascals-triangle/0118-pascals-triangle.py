class Solution(object):
    def generate(self, numRows):
        output_triangle = []
        for i in range(1,numRows+1):
            output_triangle.append([1]*i)
        for i in range(2 , numRows):
            for j in range(1,i):
                output_triangle[i][j]=output_triangle[i-1][j]+output_triangle[i-1][j-1]
        return output_triangle

