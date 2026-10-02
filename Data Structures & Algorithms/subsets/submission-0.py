class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []

        #for each object we can either choose to include it or not
        def backtrack(current, i):
            if i == len(nums):
                results.append(current.copy())
                return
            current.append(nums[i])
            backtrack(current, i + 1)
            current.pop()
            backtrack(current,i+1)

        backtrack([],0)
        return list(results)
        