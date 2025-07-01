class Solution(object):
    def possibleStringCount(self, word):
        count = 1
        for i in range(0,len(word)-1):
            if word[i]==word[i+1]:
                count+=1
        return count
        