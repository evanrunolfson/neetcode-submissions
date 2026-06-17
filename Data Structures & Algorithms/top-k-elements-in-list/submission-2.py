class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        for i in nums:
            frequency[i] = 1 + frequency.get(i, 0) #frequency[1] = ...

        pairs = []

        for i in frequency: #1, 2, 2, 3, 3, 3
            pairs.append([frequency[i], i]) #1 (value), 1 (key)
        
        pairs.sort() #[[1, 1], [2, 2], [3, 3]]
        pairs.reverse() #[[3, 3], [2, 2], [1, 1]]

        results = []
        for i in range(k):
            results.append(pairs[i][1]) #grab the second value in each pair

        return results

