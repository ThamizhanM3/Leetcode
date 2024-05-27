class Solution:
    def romanToInt(self, s):
        x = 0
        n = len(s)
        for i in range(n):
            if i < n-1:
                if s[i] == "I" and s[i+1] == "V":
                    print("hi")
                    x -= 1
                    continue
                if s[i] == "I" and s[i+1] == "X":
                    x -= 1
                    continue
                if s[i] == "X" and s[i+1] == "L":
                    x -= 10
                    continue
                if s[i] == "X" and s[i+1] == "C":
                    x -= 10
                    continue
                if s[i] == "C" and s[i+1] == "D":
                    x -= 100
                    continue
                if s[i] == "C" and s[i+1] == "M":
                    x -= 100
                    continue
            if s[i] == "I":
                x += 1
                continue
            if s[i] == "V":
                x += 5
                continue
            if s[i] == "X":
                x += 10
                continue
            if s[i] == "L":
                x += 50
                continue
            if s[i] == "C":
                x += 100
                continue
            if s[i] == "D":
                x += 500
                continue
            if s[i] == "M":
                x += 1000
                continue
        return x
        