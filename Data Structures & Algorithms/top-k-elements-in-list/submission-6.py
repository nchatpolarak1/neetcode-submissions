class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n buckets since we know 
        # first init a count map (k=n, v=count)
        # second init a freq list where index = [list of nums where count = index]
        # [[1, 2], 3]
        # third loop through list from back to front
        # break while k = index, 

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        for n, cnt in count.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

            if len(res) == k:
                return res