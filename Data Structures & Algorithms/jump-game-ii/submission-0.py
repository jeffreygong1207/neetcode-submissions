class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        #always take the jump that gets the furthest
        l = r = 0

        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r+1):
                furthest = max(furthest, i+nums[i])
            jumps += 1
            l = r+1
            r = furthest
        return jumps
        