class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        for i in strs:
            a.append([sorted(i), i])
        a.sort()
        i = 0
        n = len(a)
        b = []
        c = []
        while i < n-1:
            if a[i][0] == a[i+1][0]:
                c.append(a[i][1])
            else:
                c.append(a[i][1])
                b.append(c)
                c = []
            i += 1
        c.append(a[i][1])
        b.append(c)
        c = []
        return b