class Solution:
    def setZeroes(self, matrix):
        mat = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    mat.append([i, j])
        for i in mat:
            for j in range(n):
                matrix[i[0]][j] = 0
            for j in range(m):
                matrix[j][i[1]] = 0