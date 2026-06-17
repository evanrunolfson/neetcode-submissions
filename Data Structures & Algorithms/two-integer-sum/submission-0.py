class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dict = {}

        for i in range(len(nums)):
            current_num = nums[i]
            needed = target - current_num #needed = 4
            
            if needed in num_dict:
                return [num_dict[needed], i] #num_dict[needed] gets the key (the number) and returns its index
                
            num_dict[current_num] = i 

        return False 