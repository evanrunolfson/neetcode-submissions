class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        return s_dict == t_dict

        #s[i] returns the letter at index 0. Like r.
        
        #if we want to print keys:
        # for i in s_dict:
        #   print(i)

        #s_dict[s[i]] -> Find val at s_dict['r' (s[0] is r)]. Python looks for the key 'r' and returns its value.
        #print(s_dict[s[i]]) prints the value at the key
            
        
        
        