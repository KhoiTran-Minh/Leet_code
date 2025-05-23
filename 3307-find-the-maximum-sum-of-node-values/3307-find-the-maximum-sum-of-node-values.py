import math

class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        max_sum = 0
        flipped_count = 0
        min_abs_diff = float('inf')
        for num in nums:
            flipped_num = num ^ k

            if flipped_num > num:
                max_sum += flipped_num
                flipped_count += 1
            else:
                max_sum += num
            min_abs_diff = min(min_abs_diff, abs(flipped_num - num))

        if flipped_count % 2 == 0:
            return max_sum
        else:
            return max_sum - min_abs_diff

