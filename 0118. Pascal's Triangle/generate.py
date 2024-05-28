class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        op = [[] for i in range(numRows)]
        op[0] = [1]
        op[1] = [1, 1]
        for i in range(2, numRows):
            op[i].append(1)
            for j in range(1, i):
                op[i].append(op[i-1][j-1]+op[i-1][j])
            op[i].append(1)
        return op