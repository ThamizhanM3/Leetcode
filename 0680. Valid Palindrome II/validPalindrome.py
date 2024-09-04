class Solution:
    def validPalindrome(self, s: str) -> bool:
        a = [i for i in s]
        i = 0
        j = -1
        n = len(a)
        while i < n:
            if a[i] == a[j]:
                i += 1
                j -= 1
            else:
                if n > 6:
                    if a[i] == a[j-1] and a[i+1] == a[j-2] and a[i+2] == a[j-3]:
                        a.pop(j)
                    else:
                        a.pop(i)
                else:
                    if a[i] == a[j-1]:
                        a.pop(j)
                    else:
                        a.pop(i)
                return True if a == a[::-1] else False
        return True