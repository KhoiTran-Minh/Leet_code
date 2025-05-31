class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)

        # Convert 2D board to 1D array
        def get_board_position(s):
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (square, steps)

        while queue:
            curr, steps = queue.popleft()
            for move in range(1, 7):
                next_square = curr + move
                if next_square > n * n:
                    continue
                r, c = get_board_position(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return steps + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, steps + 1))

        return -1
        