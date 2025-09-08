class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1,n):
            a=i
            b=n-i
            if '0' in str(a) or '0' in str(b):
                pass
            else:
                break
        return a,b
        