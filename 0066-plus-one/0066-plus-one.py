class Solution(object):
    def plusOne(self, digits):
        temp = 0
        for i in range(0,len(digits)):
            temp += digits[i]*(10**(len(digits)-i-1))
        temp+=1
        digits=[]
        for digit in str(temp):
            digits.append(int(digit))
        return digits
        
        