class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0

        for i in range(len(nums)):
            if furthest < i:
                break
            distance = nums[i]
            furthest = max(i+distance, furthest)


        if furthest >= len(nums) - 1:
            return True
        return False




        