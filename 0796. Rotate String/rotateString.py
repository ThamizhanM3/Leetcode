class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False



class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            s = [i for i in s]
            s.append(s.pop(0))
            if "".join(s) == goal:
                return True
        return False