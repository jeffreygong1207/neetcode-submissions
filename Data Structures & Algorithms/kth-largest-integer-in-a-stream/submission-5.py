import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.length = k
        heapq.heapify(self.nums)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.length:
            heapq.heappop(self.nums)
        return self.nums[0]

        
