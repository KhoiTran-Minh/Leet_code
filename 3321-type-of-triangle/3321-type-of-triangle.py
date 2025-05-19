class Solution(object):
    def triangleType(self, nums):
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        elif a == b and b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
        