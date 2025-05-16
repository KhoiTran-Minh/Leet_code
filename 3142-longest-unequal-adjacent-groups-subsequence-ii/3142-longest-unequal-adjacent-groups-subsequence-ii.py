class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        def hamming_distance(a, b):
            return sum(x != y for x, y in zip(a, b))

        n = len(words)
        dp = [[i] for i in range(n)]  # dp[i] stores the best path ending at i

        for i in range(n):
            for j in range(i):
                if (
                    groups[j] != groups[i] and
                    len(words[j]) == len(words[i]) and
                    hamming_distance(words[j], words[i]) == 1
                ):
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [i]

        # Get the longest path
        best = max(dp, key=len)
        return [words[i] for i in best]
