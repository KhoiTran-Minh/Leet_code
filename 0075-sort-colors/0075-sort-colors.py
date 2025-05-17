class Solution(object):
    def sortColors(self, nums):
        color_counts = {0: 0, 1: 0, 2: 0}

        for num in nums:
            color_counts[num] = color_counts.get(num, 0) + 1

        index = 0
        for color in sorted(color_counts.keys()):  
            count = color_counts[color]
            for _ in range(count):
                nums[index] = color
                index += 1