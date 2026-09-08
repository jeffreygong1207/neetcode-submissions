class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        for number in nums:
            counter[number] = 1 + counter.get(number, 0)
        

        arr = []
        for number, count, in counter.items():
            arr.append([count, number])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])

        return result
            
        