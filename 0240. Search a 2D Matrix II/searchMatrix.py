class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = [i for j in matrix for i in j]
        return target in x