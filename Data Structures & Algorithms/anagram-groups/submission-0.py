class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #in other one, we went through s and t and checked... for i in range(len(s))
        #for this one, we need to go through a whole array, and possibly each string in the array?

        dict_map = {}

        for i in strs: #i at 0 gives "act", i at 1 gives "pots", i at 2 gives "tops", etc...
            #sort each i/string and add it to a dictionary
            
            sort = "".join(sorted(i)) #transforms ['a', 'c', 't'] into "act"

            if sort in dict_map:
                #put them in their own array
                dict_map[sort].append(i)

            else:
                dict_map[sort] = [i]  #using [] tells dict there can be more than one val for key


        return list(dict_map.values())
            