class Solution(object):
    def colorTheGrid(self, m, n):
        mod = 10**9 + 7

        if m > n:
            m, n = n, m

        def get_valid_cols(rows):
            valid = set()

            def generate(index, current_col):
                if index == rows:
                    valid.add(tuple(current_col))
                    return

                for color in range(3):
                    if index > 0 and current_col[-1] == color:
                        continue
                    current_col.append(color)
                    generate(index + 1, current_col)
                    current_col.pop()

            generate(0, [])
            return list(valid)

        valid_cols = get_valid_cols(m)
        dp = {col: 1 for col in valid_cols}

        for _ in range(n - 1):
            next_dp = {col: 0 for col in valid_cols}
            for current_col in valid_cols:
                for prev_col in valid_cols:
                    adjacent = True
                    for i in range(m):
                        if current_col[i] == prev_col[i]:
                            adjacent = False
                            break
                    if adjacent:
                        next_dp[current_col] = (next_dp[current_col] + dp[prev_col]) % mod
            dp = next_dp

        return sum(dp.values()) % mod