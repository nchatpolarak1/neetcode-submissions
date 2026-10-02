class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for st in strs:
            charCount = [0] * 26
            for c in st:
                charCount[ord(c) - ord('a')] += 1
            res[tuple(charCount)].append(st)
        return list(res.values())