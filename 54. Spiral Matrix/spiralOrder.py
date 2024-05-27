class Solution:
    def newMat(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        matrix.pop(0)
        for i in range(m-1):
            matrix[i].pop(n-1)
        for i in range(m-1):
            matrix[i] = matrix[i][::-1]
        matrix = matrix[::-1]
        return matrix

    def spiralOrder(self, matrix):
        m = r = len(matrix)
        n = c = len(matrix[0])
        mat = []
        while m + n :
            i = 0
            for j in range(n):
                mat.append(matrix[i][j])
            for i in range (1, m):
                mat.append(matrix[i][j])
            matrix = self.newMat(matrix)
            m -= 1
            n -= 1
            if r*c == len(mat):
                return mat