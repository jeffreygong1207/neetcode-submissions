class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        results = []
        nums.sort()

        def backtrack(current, i):
            if i == len(nums):
                results.append(current.copy())
                return
            current.append(nums[i])
            backtrack(current, i +1)
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            current.pop()
            backtrack(current, i + 1)

        backtrack([],0)


        return results
        