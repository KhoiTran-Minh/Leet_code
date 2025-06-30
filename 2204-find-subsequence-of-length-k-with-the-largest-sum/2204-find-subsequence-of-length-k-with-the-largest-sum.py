class Solution(object):
    def maxSubsequence(self, nums, k):
        temp = sorted(nums,reverse=True)
        temp2 = []
        for i in range(0,k):
            temp2.append(temp[i])
        temp = []
        for i,num in enumerate(nums):
            if num in temp2:
                temp.append(i)
                temp2.pop(temp2.index(num))
        temp2 = []
        for i in temp:
            temp2.append(nums[i])
            
        return temp2            
        