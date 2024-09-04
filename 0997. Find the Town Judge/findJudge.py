class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [i[0] for i in trust]
        b = [i[1] for i in trust]
        for i in range(1, n+1):
            if i not in a and b.count(i) == n-1:
                return i
        return -1