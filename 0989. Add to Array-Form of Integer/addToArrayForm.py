class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(0)
        s = ""
        for i in num:
            s += str(i)
        n = int(s) + k
        x = str(n)
        a = []
        for i in x:
            a.append(int(i))
        return a