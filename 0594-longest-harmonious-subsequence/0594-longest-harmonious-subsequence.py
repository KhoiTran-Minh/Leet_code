class Solution(object):
    def findLHS(self, nums):
        freq_map = {}
        max_length = 0
        for num in nums:
            freq_map[num]=freq_map.get(num,0)+1

        for num in freq_map:
            if (num + 1) in freq_map:
                current_length = freq_map[num] + freq_map[num + 1]
                max_length = max(max_length, current_length)

        return max_length
        
        
        