class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        n = len(s)-1
        while i<n:
            b = s[i]
            s[i] = s[n]
            s[n] = b
            i+=1
            n-=1
        return s