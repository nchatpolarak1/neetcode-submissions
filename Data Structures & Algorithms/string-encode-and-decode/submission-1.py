class Solution:
    # 4#neet5#co#de
    # we need a integer that represents the length of the word then
    # a delimiter like # where everything to the right is the word


    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    # index for where we are
    # while index is less than length
    # j to find end of delimiter so 4#
    # set j to index
    # while the character isnt #, increment
    # then get the length which is string index from i to j ()
    # ex 4#neet
    # i = 0
    # j = 1
    # get the length which is str(i:j)

    # j + 1 = # to j + 1 + length = neet
    # append that ^
    # also move i to where the next string will be

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res



