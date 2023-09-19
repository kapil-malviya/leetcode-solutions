class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''        
        num11 = int(num1)
        num22 = int(num2)
        
        result = num11*num22
        
        return str(result)
        '''

        result = [0] * (len(num1) + len(num2))
    
        # converting string to integer in reverse order
        num1 = num1[::-1]
        num2 = num2[::-1]
    
        # multiplication digit by digit
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += int(num1[i]) * int(num2[j])
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
    
        # removing leading zeros from result
        while len(result) > 1 and result[-1] == 0:
            result.pop()
    
        # convert result list to string and reverse it
        result = ''.join(map(str, result[::-1]))
    
        return result