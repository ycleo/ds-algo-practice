# 1. verify the constraints
    # Does the capital letter exist? -> no
    # Can the string be empty? -> no, at least one letter or '#' character

# 2. Test cases
    # s = '#', t = 'a#' -> true
    # s = '#', t = 'a#b#' -> true
    # s = 'ab#c##d', t = 'd' -> true

# 3. Algorithm
    # process each string and then compare

# 4. Coding 
def process(str):
    ans = []
    for letter in str:
        if letter != '#':
            ans.append(letter) 
        else:
            if len(ans) > 0:
                ans.pop(-1)
    return ''.join(ans)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return process(s) == process(t)

# 5. check typo
# 6. Run test cases
# 7. Analyze complexity
    # time: O(m + n)
    # space: O(m + n)

# 8. Think imporved method