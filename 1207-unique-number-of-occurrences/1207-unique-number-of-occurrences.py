class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence_count = {}
        
        # count occurrences of each value in array
        for num in arr:
            occurrence_count[num] = occurrence_count.get(num, 0) + 1
            
        # check if set of occurrences is unique
        unique_occurrences = set(occurrence_count.values())
        
        return len(unique_occurrences) == len(occurrence_count)