class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop
        # complement = target - val
        # in map = {3: 0, }?
        # return [map index, complement]
        # 3

        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i
        
        return