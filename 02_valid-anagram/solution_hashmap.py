class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}

        for c in t:
            if not c in chars:
                chars[c] = 0
            chars[c] += 1

        for c in s:
            if len(chars) == 0:
                return False

            if c in chars:
                if chars[c] > 1:
                    chars[c] -= 1
                else:
                    del chars[c]

        if len(chars) > 0:
            return False
        
        return True
        
