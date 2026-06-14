class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check lengths
        # 26 arr to store count at respective letter index a = 0, b = 1 etc
        # return if balance is 0

        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False

        return True

