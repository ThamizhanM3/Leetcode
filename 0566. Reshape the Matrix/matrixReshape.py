class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        matrix = []
        for i in range(r):
            matrix.append([])
        l = 0
        count = 0
        for i in range(m):
            for j in range(n):
                matrix[l].append(mat[i][j])
                count += 1
                if count >= c:
                    count = 0
                    l += 1
        return matrix