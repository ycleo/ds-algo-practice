def process(str):
    ans = []
    for letter in str:
        if letter != '#':
            ans.append(letter) 
        else:
            if len(ans) > 0:
                del ans[-1]
    return ''.join(ans)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return process(s) == process(t)

# time: O(m + n)
# space: O(m + n)