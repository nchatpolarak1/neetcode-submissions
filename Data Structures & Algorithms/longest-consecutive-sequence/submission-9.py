class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in numSet:
                seq_length = 1
                while (num + seq_length) in numSet:
                    seq_length += 1
                res = max(res, seq_length)
        return res
        