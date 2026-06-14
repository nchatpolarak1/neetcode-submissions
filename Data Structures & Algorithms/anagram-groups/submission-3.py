class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. count[a-z] = 1e, 1a, 1t
        # 2. hashmap[count: eat, tea, ate]
        # 3. 

        # default dict so default value is a list
        # loop string in strs
        # init count array of 26 letters
        # loop character in string
        # map [a, b, ... z] = ascii of current - a, increment by 1 since its adding to current list
        
        # append to result, python need to use tuple as key (non mutable)
        # return result values

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())