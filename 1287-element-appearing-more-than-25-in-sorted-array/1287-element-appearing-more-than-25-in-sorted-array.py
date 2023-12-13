class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        # count occurrences for each unique element
        count_dict = {}

        for number in arr:
            if number in count_dict:
                count_dict[number] += 1
            else:
                count_dict[number] = 1

        # find key with maximum count
        max_count = 0
        max_count_key = 0

        # iterate through dictionary to find key with the maximum count
        for key, count in count_dict.items():
            if count > max_count:
                max_count = count
                max_count_key = key 

        return max_count_key
