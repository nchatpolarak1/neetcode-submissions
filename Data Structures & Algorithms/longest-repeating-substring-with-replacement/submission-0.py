class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounts = {}
        res = 0

        l = 0
        maxFreq = 0
        for r in range(len(s)):
            charCounts[s[r]] = 1 + charCounts.get(s[r], 0)
            maxFreq = max(maxFreq, charCounts[s[r]])

            if (r - l + 1) - maxFreq > k:
                charCounts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
