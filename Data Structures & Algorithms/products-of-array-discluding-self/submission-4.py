class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        front = 1
        front_array = []

        back = 1
        back_array = []

        length = len(nums)

        for i in range(length):
            back_i = length-1 - i
            front *= nums[i]
            back *= nums[back_i]

            #appending to array
            front_array.append(front)
            back_array.append(back)
        back_array.reverse()

        #arrays are set
        result = []
        for i in range(length):
            if i == 0:
                result.append(back_array[i+1])
            elif i == length-1:
                result.append(front_array[i-1])
            else:
                result.append(front_array[i-1]* back_array[i+1])
        return result
        