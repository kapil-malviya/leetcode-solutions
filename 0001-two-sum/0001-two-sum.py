class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary to store complement of each no. and index
        dict = {}

        for i, num in enumerate(nums) :
            complement = target - num

            # checks if complement exist in dictionary
            if complement in dict :
                return [dict[complement], i]
            # add current no. and its index to dictionary
            dict[num] = i

        # if no solution found return empty dictionary
        return []