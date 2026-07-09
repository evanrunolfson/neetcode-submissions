class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() #-4, -1, -1, 0, 1, 2

        new_list = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1 #5
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplet.sort()
                    if triplet not in new_list:
                        new_list.append(triplet)
                    left +=1
                    right -=1
                elif current_sum > 0:
                    right -=1
                else:
                    left +=1

        return new_list