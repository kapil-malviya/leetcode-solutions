class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        # if input is empty return empty list
        if not digits :
            return []
        
        # function to generate combination
        def fun(index, path) :
            if len(path) == len(digits) :
                combinations.append(path)
                return
            
            # current digit
            current_digit = digits[index]
            
            # take the letters associated with current digit
            letters = dictionary[current_digit]
            
            # take next digit and update path
            for letter in letters :
                fun(index+1, path+letter)
                
        combinations = []
        fun(0, '')
        return combinations