class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = []
        n = len(tokens)
        sym = ['+', '-', '*', '/']


        for i in range(n):
            if tokens[i] not in sym:
                a.append(tokens[i])
            elif a[-1] not in sym and a[-2] not in sym:
                match tokens[i]:
                    case '+':
                        x = int(a[-1]) + int(a[-2])
                    case '-':
                        x = int(a[-2]) - int(a[-1])
                    case '*':
                        x = int(a[-1]) * int(a[-2])
                    case '/':
                        x = int(int(a[-2]) / int(a[-1]))
                a.pop()
                a.pop()
                a.append(x)
            else:
                a.append(tokens[i])
        return int(a[0])