class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        left = 0
        longest = 0
        max_len = 0

        for right in range(len(s)): #0-5
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            print(seen)

            current_len = len(seen)
            if current_len > max_len:
                max_len = current_len

        return max_len
            