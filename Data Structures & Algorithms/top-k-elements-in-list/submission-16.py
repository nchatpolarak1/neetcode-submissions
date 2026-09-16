class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)
        
        sortedList = []
        for n, cnt in countMap.items():
            sortedList.append((cnt, n))
        
        sortedList.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(sortedList[i][1])

        return res
