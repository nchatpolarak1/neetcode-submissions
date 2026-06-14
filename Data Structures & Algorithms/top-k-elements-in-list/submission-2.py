class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #         Top K freq elements:
        # counts to store num: occurences

        # freq to store nums where the index is how many times they occur
        #     0    1    2    3 
        # ex: [], [3], [2], [1], [], [], []

        # then loop in freq list from the back to get highest frequencies(descending order)
        # loop through n in freq[i]
        # if result list length == k, return res

        # Time: O(N): may have to scan all n buckets
        # Space: O(N) creating space for hashmap and lists

        # hashmap to store counts
        # freq list every where index is the freq and value is numbers for that freq

        # Loop thru nums to update count hashmap, (num: freq)
        # add each num from count to freq list

        # loop from back to front
        # for each num in the freq add to result
        # end when the length of result is equal to k
        
        freqMap = {}
        freqList = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        for n, c in freqMap.items():
            freqList[c].append(n)

        res = []
        for i in range(len(freqList) - 1, -1, -1):
            for n in freqList[i]:
                res.append(n)
                if len(res) == k:
                    return res

        