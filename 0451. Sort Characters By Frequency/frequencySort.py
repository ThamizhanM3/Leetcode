class Solution:
    def frequencySort(self, s: str) -> str:
        a = set(s)
        b = []
        for i in a:
            b.append([s.count(i), i])
        b.sort()
        b = b[::-1]
        o = ""
        for i in b:
            for j in range(i[0]):
                o += i[1]
        return o
    # x = Counter(s)
    # print(sorted(s, key = lambda a: (x[a]), reverse = True))
    # return "".join(sorted(s, key = lambda a: (x[a]), reverse = True))


class Solution:
    def frequencySort(self, s: str) -> str:
        a = set(s)
        b = []
        for i in a:
            b.append([s.count(i), i])
        b.sort()
        b = b[::-1]
        o = ""
        for i in b:
            for j in range(i[0]):
                o += i[1]
        return o
    # x = Counter(s)
    # print(sorted(s, key = lambda a: (x[a]), reverse = True))
    # return "".join(sorted(s, key = lambda a: (x[a]), reverse = True))



class Solution:
    def frequencySort(self, s: str) -> str:
        a = set(s)
        b = []
        for i in a:
            b.append([s.count(i), i])
        b.sort()
        b = b[::-1]
        o = ""
        for i in b:
            for j in range(i[0]):
                o += i[1]
        return o