class Solution(object):
    def maxAdjacentDistance(self, nums):
        max_num = 0 
        for i in range(0,len(nums)-1):
            temp = abs(nums[i]-nums[i+1])
            if max_num<temp:
                max_num=temp

        temp = abs(nums[len(nums)-1]-nums[0])
        if max_num<temp:
            max_num=temp
        return max_num
        