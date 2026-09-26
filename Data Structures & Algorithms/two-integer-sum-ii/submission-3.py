class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0 , len(numbers) - 1

        while left < right:
            lnum = numbers[left]
            rnum = numbers[right]
            if lnum + rnum == target:
                return [left + 1, right + 1]
            elif lnum + rnum < target:
                left += 1
            else:
                right -= 1
        
        return False
        