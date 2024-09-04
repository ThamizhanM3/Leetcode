class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5, c10, c20 = 0, 0, 0
        for i in bills:
            if i == 5:
                c5 += 1
            elif i == 10 and c5 > 0:
                c5 -= 1
                c10 += 1
            elif i == 20:
                if c10 > 0 and c5 > 0:
                    c20 += 1
                    c10 -= 1
                    c5 -= 1
                elif c5 > 2:
                    c20 += 1
                    c5 -= 3
                else:
                    return False
            else:
                return False
        return True



class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5, c10, c20 = 0, 0, 0
        for i in bills:
            if i == 5:
                c5 += 1
                print(i, c5, c10, c20)
            elif i == 10 and c5 > 0:
                c5 -= 1
                c10 += 1
                print(i, c5, c10, c20)
            elif i == 20:
                if c10 > 0 and c5 > 0:
                    c20 += 1
                    c10 -= 1
                    c5 -= 1
                elif c5 > 2:
                    c20 += 1
                    c5 -= 3
                else:
                    return False
                print(i, c5, c10, c20)
            else:
                return False
        return True