class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            i = s.index('@')
            return s[0] + "*****" + s[i-1:]
        else:
            s = "".join("".join("".join("".join("".join("".join(s.split()).split('-'))).split('(')).split(')')).split('+'))
            n = len(s)
            if n == 10:
                return "***-***-" + s[6:]
            if n == 11:
                return "+*-***-***-" + s[7:]
            if n == 12:
                return "+**-***-***-" + s[8:]
            if n == 13:
                return "+***-***-***-" + s[9:]