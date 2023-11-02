class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts = {}
        n = len(nums)

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

            if counts[num] > n // 2:
                return num