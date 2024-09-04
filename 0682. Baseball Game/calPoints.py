class Solution:
    def calPoints(self, operations: List[str]) -> int:
        c = []
        for i in operations:
            if i == '+':
                c.append(c[-1] + c[-2])
            elif i == 'D':
                c.append(c[-1]*2)
            elif i == 'C':
                c.pop(-1)
            else:
                c.append(int(i))
        return sum(c)