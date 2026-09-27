class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        #find the rotation point, minimum will be next after rotation poitn
        while l < r:
            middle = (l+r)//2
            if nums[middle] > nums[r]:
                #drop is to the right
                l = middle + 1
            else:
                r = middle
        return nums[l]



