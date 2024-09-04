class Solution:
    def findWords(self, words):
        r1 = "qwertyuiop" + "qwertyuiop".upper()
        r2 = "asdfghjkl" + "asdfghjkl".upper()
        r3 = "zxcvbnm" + "zxcvbnm".upper()
        opt = []
        for i in words:
            c = 0
            for j in i:
                if j in r1:
                    c += 1
            if c == len(i):
                opt.append(i)
                c = 0
                continue
            c = 0
            for j in i:
                if j in r2:
                    c += 1
            if c == len(i):
                opt.append(i)
                c = 0
                continue
            c = 0
            for j in i:
                if j in r3:
                    c += 1
            if c == len(i):
                opt.append(i)
                c = 0
                continue
        return opt