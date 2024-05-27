class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for j in range(n)] for i in range(m-1)]
        grid.append([1 for j in range(n)])
        for i in range(m):
            grid[i][-1] = 1
        dir = [[1, 0], [0, 1]]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                x = 0
                for k in dir:
                    a = i + k[0]
                    b = j + k[1]
                    if a < m and b < n:
                        x += grid[a][b]
                grid[i][j] += x
        return grid[0][0]