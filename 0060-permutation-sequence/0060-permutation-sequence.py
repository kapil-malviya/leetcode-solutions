class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        # factorial function to calculate factorial
        def fact(num):
            if num == 0 or num ==1:
                return 1
            return num * fact(num - 1)
        
        
        # recursive function to find the kth permutation
        def findPermutation(n, k, nums):
            
            # base case: if there's only one number left return it as string
            if n == 1:
                return str(nums[0])
            
            # calculate (n-1)! 
            fact_n_1 = fact(n-1)
            
            # calculate index of the current digit to be included in the result
            index = (k - 1) // fact_n_1
            
            # get current digit and remove it from the list of available numbers
            current_num = nums.pop(index)
            
            # update k for the next iteration
            k = k - index * fact_n_1
            
            # Recursively find the remaining digits of the permutation
            return str(current_num) + findPermutation(n - 1, k, nums)
        
        # Create a list of numbers from 1 to n
        nums = list(range(1, n + 1))
        
    
        return findPermutation(n, k, nums)