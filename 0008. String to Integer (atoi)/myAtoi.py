class Solution:
    def myAtoi(self, s: str) -> int:
        x = 1
        sym = 0
        dig = 0
        opt = '0'
        for i in s:
            if i == '-':
                sym += 1
                if sym > 1:
                    break
                x = -1
            elif i == '+':
                sym += 1
                if sym > 1:
                    break
                x = 1
            elif i.isdigit():
                dig = 1
                sym = 2
                opt += i
            elif i == ' ':
                if sym == 1:
                    return 0
                if dig == 1:
                    break
                continue
            else:
                break
        n = x*int(opt)
        p = pow(2, 31)
        if n > (p-1):
            return p-1
        if n < (-1*p):
            return p*(-1)
        return n