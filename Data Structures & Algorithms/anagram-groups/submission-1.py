class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a-z

            for c in s:
                # Assigns the count of character c to the index
                # ex. a = 0, b = 1 ... because ord uses ascii values
                count[ord(c) - ord("a")] += 1

            # groups the anagrams to each frequency of letters
            # ex eat, tea, ate -> 1e 1a 1t
            res[tuple(count)].append(s)
        
        # Anagrams grouped together
        return res.values()