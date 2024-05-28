class Solution:
    def convertToTitle(self, columnNumber):
        a = []
        opt = ""
        while columnNumber:
            if columnNumber < 27:
                a.append(columnNumber)
                columnNumber -= columnNumber
            else:
                if columnNumber%26 == 0:
                    a.append(26)
                    columnNumber -= 1
                else:
                    a.append(columnNumber%26)
                columnNumber = int(columnNumber/26)
                print(columnNumber)
        
        for i in a:
            opt += chr(i + 64)
            
        opt = opt[::-1]
        
        return opt