class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = 0
        j = 1
        n = len(chars)
        while j < n:
            if chars[i] == chars[j]:
                j += 1
            elif chars[i] != chars[j]:
                s += chars[i]
                if j-i > 1:
                    s += str(j-i)
                i = j
                j += 1
        s += chars[i]
        if j-i > 1:
            s += str(j-i)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)