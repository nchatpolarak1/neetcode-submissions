class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Check if lengths are the same
        # 2. two hashmaps for s and t to track the freq of each char
        # 3. return true if both hashmaps are the same freqs

        # {r:  2, a: 2, c: 2, e: 1, 
        # {c: 2, a: 2, r: 2, e: 1}

        if len(s) != len(t):
            return False

        freqS = {}
        freqT = {}
        for i in range(len(s)):
            freqS[s[i]] = 1 + freqS.get(s[i], 0)
            freqT[t[i]] = 1 + freqT.get(t[i], 0)

        return freqS == freqT



        