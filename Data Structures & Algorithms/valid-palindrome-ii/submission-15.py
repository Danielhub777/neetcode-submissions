class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(string, l, r):
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        i = 0
        n = len(s)-1
        while i < n:
            if s[i] == s[n]:
                i += 1
                n -= 1
            else:
                return is_pal(s, i + 1, n) or is_pal(s, i, n - 1)
        return True