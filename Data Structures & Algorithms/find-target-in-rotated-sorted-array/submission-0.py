class Solution:
    def search(self, nums: List[int], target: int) -> int:


        

        n = len(nums)
        bottom = 0
        top = n - 1

        while bottom <= top:
            middle = (bottom + top)//2
            if nums[middle] == target:
                return middle
            
            #left half is sorted
            if nums[middle] >= nums[bottom]:
                if nums[bottom] <= target < nums[middle]:
                    top = middle - 1
                else:
                    bottom = middle + 1
            else:
                if nums[middle] < target <= nums[top]:
                    bottom = middle + 1
                else:
                    top = middle - 1


            
        return -1
        