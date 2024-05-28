class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = (len(matrix)*len(matrix[0]))-1
        while l <= h:
            m = (l+h)//2
            r = m//len(matrix[0])
            c = m%len(matrix[0])
            if matrix[r][c] == target:
                return True
            elif target < matrix[r][c]:
                h = m-1
            else:
                l = m+1
        return False



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = [i for j in matrix for i in j]
        return target in x