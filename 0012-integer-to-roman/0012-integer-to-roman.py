class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        roman_dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        for i in roman_dict.keys() :
            roman += roman_dict[i]*(num//i)     # adding roman symbol to result
            num = num%i                        # update no. to remaining value
            if num == 0 :
                break
        return roman