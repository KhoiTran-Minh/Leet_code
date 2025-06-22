class Solution(object):
    def divideString(self, s, k, fill):
        temp=""
        result = []
        for i in range(0,len(s)):
            temp+=s[i]
            if len(temp)==k:
                result.append(temp)
                temp=""
        while len(temp)<k and len(temp)>0:
            temp+=fill
        if len(temp)==k:
            result.append(temp)
        return result
