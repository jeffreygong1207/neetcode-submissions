class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for i in range(len(nums)):
            product *= nums[i]

        solution = [1] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                prod = 1
                for j in range(len(nums)):
                    if j == i:
                        continue
                    else:
                        prod *= nums[j]
                solution[i] = int(prod)
            else:
                solution[i] = int(product / nums[i])
        return solution

        