class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1,2] + [0]*(n-2)
        if n < 3:
            return ways[n-1]

        for i in range(2,n):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[n-1]

        