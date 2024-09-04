class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = 0
        n = len(words)
        o = []
        for j in words[0]:
            for i in range(1, n):
                if j in words[i]:
                    words[i] = [k for k in words[i]]
                    words[i].pop(words[i].index(j))
                    words[i] = "".join(words[i])
                    c += 1
            if c == n-1:
                o.append(j)
            c = 0
        return o