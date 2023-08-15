# https://leetcode.com/problems/encode-and-decode-strings/

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        for s in strs:
            encoded_str += (str(len(s)) + '#' + s)
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_list = []
        
        l, r = 0, 0
        while r < len(s):
            while s[r] != '#':
                r += 1
            currLen = int(s[l:r])
            string = s[r + 1: r + 1 + currLen]
            decoded_list.append(string)
            r = l = r + 1 + currLen
     
        return decoded_list


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
