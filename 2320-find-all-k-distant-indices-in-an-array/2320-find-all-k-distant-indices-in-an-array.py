class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        store_key_pos = []
        result = []
        for i in range(0,len(nums)):
            if nums[i]==key:
                store_key_pos.append(i)
        for i in store_key_pos:
            for j in range(0,len(nums)):
                temp = abs(j-i)
                if temp<=k:
                    result.append(j)
        del store_key_pos
        result=set(result)
        result=sorted(result)
        return result

        