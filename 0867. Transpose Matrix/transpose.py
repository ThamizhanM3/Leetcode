class Solution:
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        matrix1 = []
        for i in range(n):
            matrix1.append([])
            for j in range(m):
                matrix1[i].append(0)
        for i in range(0, m):
            for j in range(0, n):
                matrix1[j][i] = matrix[i][j]
        return matrix1