class Solution:
    def plusOne(self, digits):
        sum = 0
        digits = digits[::-1]
        for i in range(len(digits)):
            sum += pow(10, i) * digits[i]
        sum += 1
        result = [int(x) for x in str(sum)]
        return result