class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()]).lower()
        print(s)
        sReversed = s[::-1]
        return s == sReversed