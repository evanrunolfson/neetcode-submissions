class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)


        #Left Pass
        current_product = 1
        for i in range(len(nums)): #0, 1, 2, 3
            res[i] = current_product
            current_product = current_product * nums[i]

        #Right Pass
        current_product = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] = res[i] * current_product
            current_product = current_product * nums[i]

        return res