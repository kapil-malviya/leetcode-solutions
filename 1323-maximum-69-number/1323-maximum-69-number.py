class Solution:
    def maximum69Number (self, num: int) -> int:
        
        num = str(num)

        for digit in range(len(num)):
            if num[digit] == '6':
                num = num[:digit] + '9' + num[digit+1:]
                break

        return int(num)