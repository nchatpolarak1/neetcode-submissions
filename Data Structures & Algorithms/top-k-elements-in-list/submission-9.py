class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # optimal
        # array of buckets
        # index corresponds to the count,
        # get counts in a map
        # 1: 1, 2:2, 3:3
        #    0.  1.  2
        #   [ ] [1 ] [1 ]
        # loop from back to front
        # break when len res == k

        freqMap = {}
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        
        count = [[] for i in range(len(nums) + 1)]
        for n, cnt in freqMap.items():
            count[cnt].append(n)

        # [7]
        res = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                if len(res) == k:
                    return res
                res.append(n)

        return res
