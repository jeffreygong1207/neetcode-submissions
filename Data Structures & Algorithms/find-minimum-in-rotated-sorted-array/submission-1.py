class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        bottom = 0
        top = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while bottom <= top:
            middle = (bottom + top) //2
            if nums[middle] < nums[((middle - 1)%len(nums))]:
                return nums[middle]
            #left half is sorted
            if nums[middle] <= nums[top]:
                top = middle - 1
            else:
                bottom = middle + 1

        