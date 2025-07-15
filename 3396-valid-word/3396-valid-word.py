class Solution(object):

    def isValid(self, word):
        def is_vowel(char):
            vowel =  ['a','e','i','o','u']
            if char in vowel:
                return True
            return False    

        if len(word)<3:
            return False
        has_vowel= 0
        has_consonant = 0
        has_number = 0
        for char in word:
            if ord(char)>=48 and ord(char)<=57:
                has_number=1
            if ord(char.lower())>=97 and ord(char.lower())<=122:
                if is_vowel(char.lower()):
                    has_vowel=1
                else:
                    has_consonant=1
            if ord(char.lower())>57 and ord(char.lower())<97:
                return False
            if ord(char)<48 or ord(char)>122:
                return False
        if has_vowel==1 and has_consonant==1:
            return True
        return False

        
        