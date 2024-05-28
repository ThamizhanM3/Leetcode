class Solution:
    def letters(self, n):
        arr = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        return arr[n]
    def mix(self, a, b):
        arr = []
        for i in a:
            for j in b:
                arr.append(i+j)
        return arr
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        arr = [i for i in self.letters(int(digits[0]))]
        for i in range(1, len(digits)):
            b = [j for j in self.letters(int(digits[i]))]
            arr = self.mix(arr, b)
        print(arr)
        return arr