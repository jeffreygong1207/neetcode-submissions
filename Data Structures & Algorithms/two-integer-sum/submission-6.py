class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i, number in enumerate(nums):
            complement = target - number
            if complement in tracker and tracker[complement] != i:
                return [tracker[complement], i]
            tracker[number] = i
        
        return []