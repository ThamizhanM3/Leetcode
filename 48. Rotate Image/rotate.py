class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = []
        x = []
        n = len(matrix)
        for i in range(n):
            for j in range(n-1, -1, -1):
                x.append(matrix[j][i])
            m.append(x)
            x = []
        for i in range(n):
            matrix[i] = m[i]