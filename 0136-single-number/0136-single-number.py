class Solution(object):
    def singleNumber(self, nums):
        count_map={}
        for i in nums:
            count_map[i]=count_map.get(i,0)+1
        for key,value in count_map.items():
            if value==1:
                return key
        
        