class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for _ in range(len(nums) + 1)]
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1

        for n, count in freqMap.items():
            freqList[count].append(n)
        
        res = []
        for i in range(len(freqList) - 1, 0, -1):
            if len(res) == k:
                break
            for num in freqList[i]:
                res.append(num)
        return res