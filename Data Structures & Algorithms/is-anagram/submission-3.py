class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one = sorted(s)
        # two = sorted(t)
        # if one == two:
        #     return True
        # else:
        #     return False
        one = dict()
        for i in s:
            one[i] = one.get(i, 0) + 1


        for i in t:
            if i in one:
                one[i]-=1
            else:
                return False
        for i in one:
            if one[i] == 0:
                continue
            else:
                return False
        return True