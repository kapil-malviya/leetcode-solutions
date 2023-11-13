class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        common = {}
        result = []
        min_index_sum = float('inf')  # Initialize with positive infinity
        
        # dictionary to store indices of strings in list1
        for i, restaurant in enumerate(list1):
            common[restaurant] = i
            
        # find common strings
        for j, restaurant in enumerate(list2):
            if restaurant in common:
                index_sum = j + common[restaurant]
                
                # update result if current index sum is smaller
                if index_sum < min_index_sum:
                    result = [restaurant]
                    min_index_sum = index_sum
                elif index_sum == min_index_sum:
                    result.append(restaurant)
                    
        return result