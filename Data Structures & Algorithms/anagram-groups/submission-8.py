class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cntMap = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            cntMap[tuple(cnt)].append(s)

        return list(cntMap.values())
        

