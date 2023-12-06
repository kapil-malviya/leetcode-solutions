class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)

        # no. of mismatches
        count = 0

        for i in range(len(heights)):
            # check if height at current index is not equal to expected height
            if heights[i] != expected[i]:
                # if not equal, increment count
                count += 1

        return count