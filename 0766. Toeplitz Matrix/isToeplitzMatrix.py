class Solution:
    def isToeplitzMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        a = []
        l = 0
        for i in range(m+ n -1):
            a.append([])
        l = 0
        for i in range(m):
            k = i
            for j in range(n):
                if k < m:
                    a[l].append(matrix[k][j])
                    k += 1
            l += 1
        o = 1
        for i in range(1, n):
            k = i
            for j in range(m):
                if k < n:
                    a[l].append(matrix[j][k])
                    k += 1
            l += 1
            o += 1
        for i in a:
            check = i[1:] == i[:-1]
            if check == False:
                return False
        return True