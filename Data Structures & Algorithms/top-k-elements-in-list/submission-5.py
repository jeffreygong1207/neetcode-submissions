from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = Counter(nums)
        # O(n) [(value, count) , 2: 2, 3:3]
        return [number for number, value in tracker.most_common(k)]
        

        