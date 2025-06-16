class Solution(object):
    def maximumDifference(self, nums):
        dif = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dif.append(nums[j]-nums[i])
        if dif:
            return max(dif)
        return -1
        