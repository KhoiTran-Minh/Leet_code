class Solution(object):
    def largestPerimeter(self, nums):
        def iStriangle(a,b,c):
            if a + b > c and a + c > b and b + c > a:
                return True
            return False
        nums=sorted(nums)
        result = 0 
        for i in range(0,len(nums)-2):
            if iStriangle(nums[i],nums[i+1],nums[i+2]):
                result = nums[i]+nums[i+1]+nums[i+2]
        return result
        