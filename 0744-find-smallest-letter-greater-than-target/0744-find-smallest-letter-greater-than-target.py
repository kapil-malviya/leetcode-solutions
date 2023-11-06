class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left = 0
        right = len(letters) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
        # If left is still within the bounds of the array, it will point to the smallest character greater than the target.
        # Otherwise, wrap around to the first character in the array.
        return letters[left % len(letters)]