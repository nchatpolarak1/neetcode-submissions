class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sortedSList = sorted(s)
        sortedTList = sorted(t)

        for i in range(len(sortedSList)):
            if sortedSList[i] != sortedTList[i]:
                return False
        return True
