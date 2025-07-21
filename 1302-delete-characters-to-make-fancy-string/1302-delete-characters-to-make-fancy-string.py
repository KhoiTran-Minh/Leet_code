class Solution(object):
    def makeFancyString(self, s):
        new_string = ""
        for i in range(len(s)-2):
            if s[i]==s[i+1] and s[i]==s[i+2]:
                pass
            else:
                new_string+=s[i]
        new_string=new_string+s[-2:]
        return new_string
        