class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prearray = [0] * n
        postarray = [0] * n

        
        #make previous array
        current = 1
        for i in range(n):
            current = current * nums[i]
            prearray[i] = current
        

        #make post array
        current = 1
        for i in range(n-1, -1,-1):
            current = current * nums[i]
            postarray[i] = current

        print(prearray)
        print(postarray)
        answer = []
        for i in range(n):
            if i == 0:
                answer.append(postarray[1])
            elif i == n - 1:
                answer.append(prearray[-2])
            else:
                answer.append(prearray[i-1] * postarray[i + 1])
        
        return answer