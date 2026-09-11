class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        arr = []
        for num, cnt in freqMap.items():
            arr.append((cnt, num))
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res