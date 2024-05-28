class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dir = [[1, 0], [0, 1]]
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                x = []
                for k in dir:
                    a = i + k[0]
                    b = j + k[1]
                    if a < len(grid) and b < len(grid[0]):
                        x.append(grid[i][j]+grid[a][b])
                grid[i][j] = min(x) if len(x) else grid[i][j]
        return grid[0][0]