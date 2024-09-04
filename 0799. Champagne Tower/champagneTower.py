class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        op = [[] for i in range(query_row+1)]
        op[0] = [poured]
        for i in range(1, len(op)):
            for x in range(i+1):
                op[i].append(0)
            for j in range(len(op[i])-1):
                if op[i-1][j] > 1:
                    op[i][j] += (op[i-1][j]-1)/2
            for j in range(1, len(op[i])):
                if op[i-1][j-1] > 1:
                    op[i][j] += (op[i-1][j-1]-1)/2
        return op[query_row][query_glass] if op[query_row][query_glass] <= 1 else 1.000000



class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        op = [[] for i in range(query_row+1)]
        op[0] = [poured]
        for i in range(1, len(op)):
            for x in range(i+1):
                op[i].append(0)
            for j in range(len(op[i])-1):
                if op[i-1][j] > 1:
                    op[i][j] += (op[i-1][j]-1)/2
            for j in range(1, len(op[i])):
                if op[i-1][j-1] > 1:
                    op[i][j] += (op[i-1][j-1]-1)/2
        c = 0
        for i in op:
            print(i, c)
            c += 1
        return op[query_row][query_glass] if op[query_row][query_glass] <= 1 else 1.000000