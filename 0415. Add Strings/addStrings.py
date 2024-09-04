class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = []
        b = []
        c = []
        e = len(num1)
        f = len(num2)
        n = min(e, f)
        m = max(e, f)
        for i in num1:
            a.append(i)
        a = a[::-1]
        if len(a) == n:
            for i in range(n, m):
                a.append("0")
        for i in num2:
            b.append(i)
        b = b[::-1]
        if len(b) == n:
            for i in range(n, m):
                b.append("0")
        i = 0
        z = 0
        while i < m:
            x = int(a[i]) + int(b[i]) + z
            if x < 10:
                c.append(str(x))
                z = z // 10
                i += 1
                continue
            else:
                c.append(str(x%10))
                z = x // 10
                i += 1
        if z != 0:
            c.append(str(z))
        c = c[::-1]
        o = ""
        for i in c:
            o += i
        return o