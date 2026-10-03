class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(current, chosen):
            if len(current) == len(nums):
                results.append(current.copy())
                return
            for i in range(len(nums)):
                if chosen[i] == False:
                    current.append(nums[i])
                    chosen[i] = True
                    backtrack(current, chosen)
                    current.pop()
                    chosen[i] = False

            

        backtrack([], [False]*len(nums))
        return results
        