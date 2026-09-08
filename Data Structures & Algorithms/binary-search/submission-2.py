class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom = 0
        top = len(nums) - 1
        while bottom <= top:
            middle = (top + bottom) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                bottom = middle + 1
            else:
                top = middle - 1

        return -1
        