class Solution:
    def intToRoman(self, num):
        opt = ""
        while num:
            if num > 999:
                opt += "M"
                num -= 1000
                print(num/100)
            elif int(num / 100) == 9:
                opt += "CM"
                num -= 900
            elif num > 499:
                opt += "D"
                num -= 500
            elif int(num /100) == 4:
                opt += "CD"
                num -= 400
            elif num > 99:
                opt += "C"
                num -= 100
            elif int(num / 10) == 9:
                opt += "XC"
                num -= 90
            elif num > 49:
                opt += "L"
                num -= 50
            elif int(num / 10) == 4:
                opt += "XL"
                num -= 40
            elif num > 9:
                opt += "X"
                num -= 10
            elif num == 9:
                opt += "IX"
                num -= 9
            elif num > 4:
                opt += "V"
                num -= 5
            elif num == 4:
                opt += "IV"
                num -= 4
            else:
                opt += "I"
                num -= 1
        return opt