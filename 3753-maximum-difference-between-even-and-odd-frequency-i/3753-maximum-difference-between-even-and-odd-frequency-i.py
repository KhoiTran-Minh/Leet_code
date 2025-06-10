class Solution(object):
    def maxDifference(self, s):
        key_count = {}
        for char in s:
            key_count[char]= key_count.get(char,0)+1
        s=list(set(s))
        even = []
        odd=[]
        for char in s:
            temp = key_count[char]
            if temp%2==1:
                odd.append(temp)
            if temp%2==0:
                even.append(temp)
                
        return max(odd)-min(even)
        