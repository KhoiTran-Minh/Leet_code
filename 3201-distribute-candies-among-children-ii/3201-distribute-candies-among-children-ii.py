class Solution(object):
    def distributeCandies(self, n, limit):
        def comb2(x):
            return x * (x - 1) // 2 if x >= 0 else 0

        total = comb2(n + 3 - 1)
        over1 = comb2(n - (limit + 1) + 3 - 1)
        over2 = comb2(n - 2 * (limit + 1) + 3 - 1)
        over3 = comb2(n - 3 * (limit + 1) + 3 - 1)

        return total - 3 * over1 + 3 * over2 - over3
        