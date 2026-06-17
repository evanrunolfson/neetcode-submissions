class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dictionary 
        #loop through the whole list/array
        #key = number, value = increment for each time it is seen
        #return the k keys with the highest value, in ascending order

        dictionary = {}

        for i in nums:
            dictionary[i] = 1 + dictionary.get(i, 0)

        list = []

        for i in dictionary:
            list.append([dictionary[i], i]) # 3,3,3,3 -> 4, 3
        
        list.sort() #4, 3 would be at the end
        list.reverse() #4, 3 would be at the start

        res = []
        for i in range(k):
            res.append(list[i][1]) #grab the second value in each pair

        return res

