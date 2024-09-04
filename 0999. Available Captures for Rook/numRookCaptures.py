class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        ct = 0
        for c, i in enumerate(board):
            for d, j in enumerate(i):
                if j == 'R':
                    rp = [c, d]
        for i in range(rp[0], n):
            if board[i][rp[1]] == 'p':
                ct += 1
                break
            if board[i][rp[1]] == 'B':
                break
        for i in range(rp[0], -1, -1):
            if board[i][rp[1]] == 'p':
                ct += 1
                break
            if board[i][rp[1]] == 'B':
                break
        for i in range(rp[1], m):
            if board[rp[0]][i] == 'p':
                ct += 1
                break
            if board[rp[0]][i] == 'B':
                break
        for i in range(rp[1], -1, -1):
            if board[rp[0]][i] == 'p':
                ct += 1
                break
            if board[rp[0]][i] == 'B':
                break
        return ct