class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        s = 0
        for i in grid:
            s += sum(i)
        s *= 4
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for k in dir:
                    nr = i + k[0]
                    nc = j + k[1]
                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1 and grid[i][j] == 1:
                        s -= 1
        return s