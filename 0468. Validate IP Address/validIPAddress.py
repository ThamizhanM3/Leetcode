class Solution:
    def check4(self, queryIP):
        a = queryIP.split('.')
        if len(a) != 4:
            return False
        for i in range(4):
            for j in a[i]:
                if j < '0' or  j > '9':
                    return False
            if a[i] == '':
                return False
            if int(a[i]) < 0 or int(a[i]) > 255:
                return False
            a[i] = str(int(a[i]))
        x = '.'.join(a)
        if len(x) != len(queryIP):
            return False
        return True
    
    def check6(self, queryIP):
        a = queryIP.split(':')
        if len(a) != 8:
            return False
        for i in a:
            if len(i) > 4 or len(i) < 1:
                return False
            for j in i:
                if (j < 'a' or j > 'f') and (j < 'A' or j > 'F') and (j < '0' or j > '9'):
                    return False
                if i == '':
                    return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP and self.check4(queryIP):
            return 'IPv4'
        elif ':' in queryIP and self.check6(queryIP):
            return 'IPv6'
        else:
            return 'Neither'