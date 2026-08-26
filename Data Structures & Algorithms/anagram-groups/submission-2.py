class Solution:
    from collections import Counter 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        things = dict()
        for i in strs:
            alpha = [0]*26
            for char in i:
                alpha[ord(char) - ord('a')]+=1
            if tuple(alpha) in things:
                things[tuple(alpha)].append(i)
            else:
                things[tuple(alpha)] = [i]
            # if tuple(Counter(i)) in things:
            #     things[tuple(Counter(i))].append(i)
            # else:
            #     things[tuple(Counter(i))] = [i]

        output = []
        for i in things:
            output.append(things[i])
        return output 


        