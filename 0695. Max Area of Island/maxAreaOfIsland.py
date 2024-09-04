class Solution:
    def __init__(self):
        self.c = 1
    def dfs(self, grid, i, j):
        if grid[i][j] == 1:
            grid[i][j] = 0
            self.c += 1
            if j+1 < len(grid[0]):
                self.dfs(grid, i, j+1)
            if i+1 < len(grid):
                self.dfs(grid, i+1, j)
            if j-1 >= 0:
                self.dfs(grid, i, j-1)
            if i+-1 >= 0:
                self.dfs(grid, i-1, j)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        opt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if j+1 < len(grid[0]):
                        self.dfs(grid, i, j+1)
                    if i+1 < len(grid):
                        self.dfs(grid, i+1, j)
                    if j-1 >= 0:
                        self.dfs(grid, i, j-1)
                    if i+-1 >= 0:
                        self.dfs(grid, i-1, j)
                    opt = max(opt, self.c)
                    self.c = 1
        return opt



class Solution:
    def __init__(self):
        self.opt = [0]
        self.c = 1
    def dfs(self, grid, i, j):
        if grid[i][j] == 1:
            grid[i][j] = 0
            self.c += 1
            if j+1 < len(grid[0]):
                self.dfs(grid, i, j+1)
            if i+1 < len(grid):
                self.dfs(grid, i+1, j)
            if j-1 >= 0:
                self.dfs(grid, i, j-1)
            if i+-1 >= 0:
                self.dfs(grid, i-1, j)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if j+1 < len(grid[0]):
                        self.dfs(grid, i, j+1)
                    if i+1 < len(grid):
                        self.dfs(grid, i+1, j)
                    if j-1 >= 0:
                        self.dfs(grid, i, j-1)
                    if i+-1 >= 0:
                        self.dfs(grid, i-1, j)
                    c += 1
                    self.opt.append(self.c)
                    self.c = 1
        return max(self.opt)



class Solution:
    def __init__(self):
        self.opt = []
        self.c = 1
    def dfs(self, grid, i, j):
        if grid[i][j] == 1:
            grid[i][j] = 0
            self.c += 1
            if j+1 < len(grid[0]):
                self.dfs(grid, i, j+1)
            if i+1 < len(grid):
                self.dfs(grid, i+1, j)
            if j-1 >= 0:
                self.dfs(grid, i, j-1)
            if i+-1 >= 0:
                self.dfs(grid, i-1, j)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if j+1 < len(grid[0]):
                        self.dfs(grid, i, j+1)
                    if i+1 < len(grid):
                        self.dfs(grid, i+1, j)
                    if j-1 >= 0:
                        self.dfs(grid, i, j-1)
                    if i+-1 >= 0:
                        self.dfs(grid, i-1, j)
                    c += 1
                    self.opt.append(self.c)
                    self.c = 1
        return 0 if len(self.opt) == 0 else max(self.opt)