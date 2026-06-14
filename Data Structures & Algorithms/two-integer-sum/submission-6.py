class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = {3: 0, 4: 1, 5: 2, 6: 3}
        # diff = target - curr
        # if curr in seen
        # return that index

        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]

            seen[nums[i]] = i
