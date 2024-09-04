class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        a = s1+s2
        c = Counter(a)
        o = []
        for i, c in c.items():
            if c == 1:
                o.append(i)
        return o