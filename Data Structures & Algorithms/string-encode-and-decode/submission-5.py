class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res

        for s in strs:
            res += str(len(s)) +'#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        if not s:
            return res
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            i = j + 1 # start of new word
            j = i + length # up until end of word
            word = s[i:j]
            res.append(word)

            i = j # i now starts at end of word
        return res

