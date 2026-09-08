class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mappingDict = {}

        for number in nums:
            if number not in mappingDict:
                mappingDict[number] = 1
            else:
                mappingDict[number] += 1
        
        arr = []
        for num, count in mappingDict.items():
            arr.append([count, num])
        arr.sort()
        
        result = []
        while len(result) < k:
            result.append(arr.pop()[1])

        return result