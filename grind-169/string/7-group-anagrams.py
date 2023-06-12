# https://leetcode.com/problems/group-anagrams/
# group_ map = {
#     "bat": [bat],
#     "eat": [ate, eat, tea],
#     "tan": [nat, tan]
# }

# map keys need to be "tuple"

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            group_map[tuple(count)].append(s)

        return group_map.values()

# O(NK)    N: len(strs), K: max length of a str in strs
# O(NK)
