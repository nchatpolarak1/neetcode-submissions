class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen: # found dupe
                return True       
            seen.add(n)
        return False         