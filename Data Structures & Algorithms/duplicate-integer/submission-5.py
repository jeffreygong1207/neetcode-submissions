class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = set()
        for number in nums:
            if number in tracker:
                return True
            tracker.add(number)
        return False