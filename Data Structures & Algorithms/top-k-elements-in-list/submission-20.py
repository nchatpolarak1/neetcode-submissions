class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        
        freqList = [[] for i in range(len(nums) + 1)]
        for n, cnt in freqMap.items():
            freqList[cnt].append(n)

        res = []
        for i in range(len(freqList) - 1, 0, -1):
            for elem in freqList[i]:
                if len(res) == k:
                    return res
                res.append(elem)

        return res
