class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0 #1
        right = len(numbers) - 1 #4


        while left < right: #while 0 < 3
            sum = numbers[left] + numbers[right] #5

            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

            

            

            