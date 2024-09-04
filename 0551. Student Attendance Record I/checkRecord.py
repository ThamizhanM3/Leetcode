class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        n = len(s)
        for i in range(n):
            if a == 2:
                return False
            if s[i] =='L':
                if i+2 < n and s[i+1] == 'L' and s[i+2] == 'L':
                    return False
            if s[i] == 'A':
                a += 1
        if a == 2:
            return False
        return True