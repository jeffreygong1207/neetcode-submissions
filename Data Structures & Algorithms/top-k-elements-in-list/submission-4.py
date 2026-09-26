from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        tracker = Counter(nums)
        return [number for number, _ in tracker.most_common(k)]
        

        