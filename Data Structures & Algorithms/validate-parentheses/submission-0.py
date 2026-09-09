class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        stack = []
        for character in s:
            if character in ['(', '[', '{']:
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False
                topelement = stack.pop()
                if character == mapping[topelement]:
                    continue
                else:
                    return False
        return len(stack) == 0

