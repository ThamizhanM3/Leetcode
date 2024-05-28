class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        op = [[] for i in range(rowIndex+1)]
        op[0] = [1]
        op[1] = [1, 1]
        for i in range(2, rowIndex+1):
            op[i].append(1)
            for j in range(1, i):
                op[i].append(op[i-1][j-1]+op[i-1][j])
            op[i].append(1)
        return op[rowIndex]