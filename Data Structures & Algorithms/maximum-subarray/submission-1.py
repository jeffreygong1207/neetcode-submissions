class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        largest = 0
        current = 0
        for r in range(len(nums)):
            #idea is keep going until negative, if negative then we discard and start from scratch (set r == 0)
            current += nums[r]
            if current < 0:
                #discard
                current = 0
            largest = max(largest, current)
            
        if largest == 0:
            largest = max(nums)

        return largest
        