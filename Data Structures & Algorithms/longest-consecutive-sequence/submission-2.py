class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #create set
        num_set = set()

        #run through list and add each num to set
        for num in nums:
            num_set.add(num)

        #initialize high score
        longest_streak = 0

        for num in num_set:
            if (num-1) not in num_set:
                current_streak = 1
                current_num = num

                while ((current_num + 1) in num_set):
                    current_streak += 1
                    current_num += 1
        
                if current_streak > longest_streak:
                    longest_streak = current_streak

        return longest_streak
