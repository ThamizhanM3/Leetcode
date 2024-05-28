class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split()
        a = a[::-1]
        c = ""
        for i in a:
            c += i + " "
        return c.strip()