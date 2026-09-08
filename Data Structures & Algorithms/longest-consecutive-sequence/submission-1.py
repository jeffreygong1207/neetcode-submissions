class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapping = set(nums)
        longest = 0

        for number in mapping:
            if (number - 1) not in mapping:
                length = 1
                while (number + length) in mapping:
                    length += 1
                longest = max(length, longest)
        
        return longest
            



        return longest
        