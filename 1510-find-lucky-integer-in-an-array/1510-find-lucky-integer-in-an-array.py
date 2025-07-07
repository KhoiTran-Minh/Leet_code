class Solution(object):
    def findLucky(self, arr):
        lucky_map={}
        for i in arr:
            lucky_map[i]=lucky_map.get(i,0)+1
        lucky_number = -1
        for key,value in lucky_map.items():
            if key==value:
                lucky_number=key
        return lucky_number