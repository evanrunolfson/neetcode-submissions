class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        for i in nums:
            frequency[i] = 1 + frequency.get(i, 0)

        pairs = []

        for i in frequency:
            pairs.append([frequency[i], i]) # 3,3,3,3 -> 4, 3
        
        pairs.sort() #4, 3 would be at the end
        pairs.reverse() #4, 3 would be at the start

        results = []
        for i in range(k):
            results.append(pairs[i][1]) #grab the second value in each pair

        return results

