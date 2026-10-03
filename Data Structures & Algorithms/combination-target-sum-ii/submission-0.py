class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        candidates.sort()

        def backtrack(current, target, i):
            if target == 0:
                results.append(current.copy())
                return
            if target < 0 or len(candidates) == i:
                return 
            current.append(candidates[i])
            backtrack(current, target-candidates[i], i + 1)
            current.pop()
            while i +1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(current, target, i+1)

        backtrack([], target, 0)
        return results
        