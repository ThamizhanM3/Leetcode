class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        c = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                c += 1
                i += 1
            j += 1
        return c == len(s)



class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        x = 0
        for i in s:
            for j in range(j, len(t)):
                print(i, j)
                if t[j] == i:
                    x += 1
                    j += 1
                    break
        return True if x == len(s) else False