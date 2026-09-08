class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tracker = set(nums)

        longest = 0


        for number in nums:
            if number -1 not in tracker:
                #we can start counting
                i = number
                while i + 1 in tracker:
                    i = i + 1
                total = i - number + 1
                longest = max(longest, total)
            else:
                continue



        return longest