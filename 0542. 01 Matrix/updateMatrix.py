class Solution:
    def __init__(self):
        self.que = []
        self.visited = []
        self.dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    
    def bfs(self):
        n = len(self.que)
        for z in range(n):
            for k in self.dir:
                r = self.que[0][0] + k[0]
                c = self.que[0][1] + k[1]
                if r >= 0 and c >= 0 and r < len(self.mat) and c < len(self.mat[0]) and not self.visited[r][c]:
                    self.visited[r][c] = True
                    self.que.append([r, c])
                    self.mat[r][c] += self.mat[self.que[0][0]][self.que[0][1]]
            self.que.pop(0)
        if len(self.que):
            self.bfs()


    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         arr = []
        #         for k in dir:
        #             r = i + k[0]
        #             c = j + k[1]
        #             if r >= 0 and c >= 0 and r < len(mat) and c < len(mat[0]):
        #                 arr.append(mat[r][c])
        #         if mat[i][j] > 0:
        #             mat[i][j] += min(arr)
        # return mat
        self.mat = mat
        for i in range(len(mat)):
            arr = []
            for j in range(len(mat[0])):
                arr.append(False)
                if mat[i][j] == 0:
                    arr[j] = True
                    self.que.append([i, j])
            self.visited.append(arr)
        self.bfs()
        return self.mat