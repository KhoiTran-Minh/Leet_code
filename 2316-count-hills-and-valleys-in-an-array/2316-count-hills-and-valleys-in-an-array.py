class Solution(object):
    def countHillValley(self, nums):
        n = len(nums)
        count = 0

        # Remove consecutive duplicates for easier processing
        filtered = [nums[0]]
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                filtered.append(nums[i])

        # Check each non-edge index
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1  # Hill
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1  # Valley

        return count