class Solution:
    def dfs(self, grid, i, j):
        if grid[i][j] == '1':
            grid[i][j] = '0'
            if j+1 < len(grid[0]):
                self.dfs(grid, i, j+1)
            if i+1 < len(grid):
                self.dfs(grid, i+1, j)
            if j-1 >= 0:
                self.dfs(grid, i, j-1)
            if i+-1 >= 0:
                self.dfs(grid, i-1, j)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    if j+1 < len(grid[0]):
                        self.dfs(grid, i, j+1)
                    if i+1 < len(grid):
                        self.dfs(grid, i+1, j)
                    if j-1 >= 0:
                        self.dfs(grid, i, j-1)
                    if i+-1 >= 0:
                        self.dfs(grid, i-1, j)
                    c += 1
        return c



class Solution:
    def dfs(self, i, j):
        if self.grid[i][j] == '1':
            self.grid[i][j] = '0'
            if j+1 < len(self.grid[0]):
                self.dfs(i, j+1)
            if i+1 < len(self.grid):
                self.dfs(i+1, j)
            if j-1 >= 0:
                self.dfs(i, j-1)
            if i+-1 >= 0:
                self.dfs(i-1, j)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        c = 0
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == '1':
                    self.grid[i][j] = '0'
                    if j+1 < len(grid[0]):
                        self.dfs(i, j+1)
                    if i+1 < len(grid):
                        self.dfs(i+1, j)
                    if j-1 >= 0:
                        self.dfs(i, j-1)
                    if i+-1 >= 0:
                        self.dfs(i-1, j)
                    c += 1
        return c