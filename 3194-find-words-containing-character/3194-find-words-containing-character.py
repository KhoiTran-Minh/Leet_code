class Solution(object):
    def findWordsContaining(self, words, x):
        pos=[]
        for i in range(0,len(words)):
            if x in words[i]:
               pos.append(i)
        return pos
        