class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        freqMap = {}
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)

        for n, cnt in freqMap.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
        return res