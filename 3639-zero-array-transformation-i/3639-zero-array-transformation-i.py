import collections

class Solution:
  def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
    n = len(nums)
    if n == 0:
      return True

    diff = collections.defaultdict(int)

    for l, r in queries:
      if l < 0 or r >= n or l > r : 
          pass
      
      diff[l] += 1
      if r + 1 < n: 
        diff[r + 1] -= 1
    current_coverage = 0
    for i in range(n):
      current_coverage += diff[i] 
      if nums[i] > current_coverage:
        return False
        
    return True