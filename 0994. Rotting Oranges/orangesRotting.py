class Solution:
    def __init__(self):
        self.que = []
        self.c = 0
        self.dir = [[0, 1], [1, 0], [-1, 0] ,[0, -1]]

    def bfs(self):
        n = len(self.que)
        for z in range(n):
            for k in self.dir:
                i = self.que[0][0]+k[0]
                j = self.que[0][1]+k[1]
                if i >= 0 and j >= 0 and i < len(self.grid) and j < len(self.grid[0]) and self.grid[i][j] == 1:
                    self.que.append([i, j])
                    self.grid[i][j] = 2
            self.que.pop(0)
        if len(self.que):
            self.c += 1
            self.bfs()


    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 2:
                    self.que.append([i, j])
        if len(self.que):
            self.bfs()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 1:
                    return -1
        return self.c