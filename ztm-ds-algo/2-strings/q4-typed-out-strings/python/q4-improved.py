# 1. verify the constraints
    # Does the capital letter exist? -> no
    # Can the string be empty? -> no, at least one letter or '#' character

# 2. Test cases
    # s = '#', t = 'a#' -> true
    # s = '#', t = 'a#b#' -> true
    # s = 'ab#c##d', t = 'd' -> true (important case!!)
    
# 3. Algorithm
    # two pointer at the end of each string -> sp, tp
    # while true:
        # process string s
        # process string t
        # if (sp >= 0) and (tp >= 0) and (sp letter == tp letter) -> sp-- and tp--
        # else -> break
    # return (sp == -1 and tp == -1)

    # How to process? backspace condition: (char == '#' or backcount > 0)
    
# 4. coding
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sp = len(s) - 1
        tp = len(t) - 1
        
        while True:
            backcount = 0
            while sp >= 0 and (s[sp] == '#' or backcount > 0):
                if s[sp] == '#':
                    backcount += 1
                else: 
                    backcount -= 1
                sp -= 1
            
            backcount = 0
            while tp >= 0 and (t[tp] == '#' or backcount > 0):
                if t[tp] == '#':
                    backcount += 1
                else: 
                    backcount -= 1
                tp -= 1
            
            if sp >= 0 and tp >= 0 and s[sp] == t[tp]:
                sp -= 1
                tp -= 1
            else:
                break
                
        return sp == -1 and tp == -1


# 5. check typo

# 6. Run test cases 
    # s = '#', t = 'a#' 
        # s[sp] = '#', sp = -1, bc = 1
        # t[tp] = 'a', tp = -1, bc = 0
        # break -> true (pass)
    
    # s = '#', t = 'a#b#' 
        # s[sp] = '#', sp = -1, bc = 0
        # t[tp] = 'a', tp = -1, bc = 0
        # break -> true (pass)
        
    # s = 'ab#c##d', t = 'd' 
        # s[sp] = 'd', sp = 6, bc = 0
        # t[tp] = 'd', tp = 0, bc = 0
        # s[sp] == t[tp] -> sp = 5, tp = -1
        
        # s[sp] = 'a', sp = -1, bc = 0
        # break -> true (pass)

# 7. Analyze complexity
    # time: O(n + m)
    # space: O(1)
    
# 8. Think improved method