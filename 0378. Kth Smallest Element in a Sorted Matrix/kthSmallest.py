class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        e = 1
        while e > 0:
            for i in range(1, n):
                while matrix[i][0] < matrix[i-1][-1]:
                    e += 1
                    matrix[i][0], matrix[i-1][-1] = matrix[i-1][-1], matrix[i][0]
                    matrix[i].sort()
                    matrix[i-1].sort()
                e -= 1
        a = (k-1) // n
        b = (k-1) % n
        #print(a, b, matrix[a][b])
        #return 0
        return matrix[a][b]