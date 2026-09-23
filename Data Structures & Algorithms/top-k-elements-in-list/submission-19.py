class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]

        freqMap = {}
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        
        for n, cnt in freqMap.items():
            freq[cnt].append(n)

        # return freq
        res = []
        for i in range(len(freq) - 1, -1, -1):
            if len(res) == k:
                return res

            for num in freq[i]:
                res.append(num)
            
        return res


        