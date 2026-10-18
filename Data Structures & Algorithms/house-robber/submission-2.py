class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        money = [0] * len(nums)
        money[0] = nums[0]
        money[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            money[i] = max(money[i-2]+nums[i], money[i-1])

        return max(money[-1], money[-2])



        