class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        n = len(s)-1
        while i < n:
            while not s[i].isalnum() and i<n:
                i+=1
            while not s[n].isalnum() and n>i:
                n-=1
            if s[i] == s[n]:
                i+=1
                n-=1
            else:
                return False
        return True 