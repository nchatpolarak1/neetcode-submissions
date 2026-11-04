class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in numMap:
                return [numMap[comp], i]
            numMap[n] = i
        return []