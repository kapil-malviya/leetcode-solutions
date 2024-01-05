class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # store frequency of each element
        frequency_map = Counter(nums)

        # Variable to store minimum operations required
        minimum_operations = 0

        for value in frequency_map.values():
            
            # if any value is 1, it means there is an element occurring only once,
            # and it is not possible to group it with others, so return -1.
            if value == 1:
                return -1

            minimum_operations += (value + 2) // 3

        return minimum_operations