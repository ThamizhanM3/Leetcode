class Solution:
    def simplifyPath(self, path: str) -> str:
        a = path.split('/')
        a = [i for i in a if len(i)>0]
        # i = 0
        # while i<len(a):
        #     print(i, a)
        #     if len(a) == 0:
        #         return '/'
        #     if a[i] == '.':
        #         a.pop(i)
        #     elif a[i] == '..':
        #         a.pop(i)
        #         if i > 0:
        #             a.pop(i-1)
        #             i -= 1
        #     else:
        #         i += 1
        # return "/" + "/".join(a)
        b = []
        for i in a:
            if i == '.':
                continue
            elif i == '..' and len(b) != 0:
                b.pop()
            elif i == '..':
                continue
            else:
                b.append(i)
        return "/" + '/'.join(b)



class Solution:
    def simplifyPath(self, path: str) -> str:
        a = path.split('/')
        a = [i for i in a if len(i)>0]
        i = 0
        while i<len(a):
            print(i, a)
            if len(a) == 0:
                return '/'
            if a[i] == '.':
                a.pop(i)
            elif a[i] == '..':
                a.pop(i)
                if i > 0:
                    a.pop(i-1)
                    i -= 1
            else:
                i += 1
        return "/" + "/".join(a)