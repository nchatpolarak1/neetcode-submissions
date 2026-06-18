class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # naive loop i 
        # loop j if i == j return true once nested loop is done return false
        # O(n2), O(1)

        #optimal
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        return False