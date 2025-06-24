class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        key_positions = [i for i, num in enumerate(nums) if num == key]
        result_set = set()

        for i in key_positions:
            start = max(0, i - k)
            end = min(len(nums), i + k + 1)
            result_set.update(range(start, end))

        return sorted(result_set)

        