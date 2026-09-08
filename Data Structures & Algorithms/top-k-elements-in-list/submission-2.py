class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        for number in nums:
            counter[number] = 1 + counter.get(number, 1)
        
        arr = []
        for number, count  in counter.items():
            arr.append([count, number])
        
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])

        return result



        