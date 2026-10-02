class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        results = []
        def backtrack(current, left, i):
            if left == 0:
                results.append(current.copy())
                return
            if left < 0 or i == len(nums):
                #we failed
                return
            current.append(nums[i])
            backtrack(current, left-nums[i], i)
            current.pop()
            backtrack(current, left, i + 1)

        
        backtrack([], target, 0)
        return results
        