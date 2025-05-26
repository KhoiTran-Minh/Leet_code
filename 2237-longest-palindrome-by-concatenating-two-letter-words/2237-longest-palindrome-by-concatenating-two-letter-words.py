from collections import Counter
class Solution(object):
    def longestPalindrome(self, words):
        count = Counter(words)
        length = 0
        used_middle = False

        for word in list(count.keys()):
            rev = word[::-1]
            if word == rev:
                pairs = count[word] // 2
                length += pairs * 4
                count[word] -= pairs * 2
            else:
                min_pair = min(count[word], count[rev])
                length += min_pair * 4
                count[word] -= min_pair
                count[rev] -= min_pair

        for word in count:
            if word[0] == word[1] and count[word] > 0:
                length += 2
                break  # only one center word allowed

        return length
        