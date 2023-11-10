class Solution:
    def maxPower(self, s: str) -> int:
        max_count = 0
        count = 1

        for char in range(1, len(s)):
            # check if current character is same as previous character
            if s[char] == s[char - 1]:
                # if found, then increment count
                count += 1
            else:
                # if it's not same character, compare count to current max_count
                if count > max_count:
                    # if the count is greater, update max_count
                    max_count = count
                # reset count to 1 for new character
                count = 1

        # check count after the loop in case maximum power extends to the end of the string
        if count > max_count:
            max_count = count

        # maximum power found
        return max_count