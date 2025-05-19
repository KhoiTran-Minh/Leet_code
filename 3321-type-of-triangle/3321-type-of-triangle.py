class Solution(object):
    def triangleType(self, nums):
        if len(nums)!=3:
            return "none"
        a=nums[0]
        b=nums[1]
        c=nums[2]
        if a+b<=c or b+c<=a or a+c<=b:
            return "none"
        if a==b and b==c:
            return "equilateral"
        if a==b or b==c or a==c:
            return "isosceles"
        if a!=b and b!=c:
            return "scalene"
        return "none"
        