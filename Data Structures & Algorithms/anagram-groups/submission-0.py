class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        things = dict()
        for i in strs:
            if tuple(sorted(i)) in things:
                things[tuple(sorted(i))].append(i)
            else:
                things[tuple(sorted(i))] = [i]
        output = []
        for i in things:
            output.append(things[i])
        return output 


        