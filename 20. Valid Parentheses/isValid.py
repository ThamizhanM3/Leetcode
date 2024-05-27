class Solution:
    def isValid(self, s):
        a = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                a.append(i)
            elif len(a) == 0:
                return False
            elif i == ')':
                if a.pop() != '(':
                    return False
            elif i == '}':
                if a.pop() != '{':
                    return False
            elif i == ']':
                if a.pop() != '[':
                    return False
        if len(a) != 0:
            return False
        return True
        