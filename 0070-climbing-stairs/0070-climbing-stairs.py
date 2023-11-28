class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        # array to store no. of ways to reach each step
        ways = [0] * (n + 1)

        # base case
        ways[1] = 1
        ways[2] = 2

        # no. of ways for each step
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]