class Solution:
    def isValid(self, s: str) -> bool:
        # mapping = {
        #     '[' : ']',
        #     '{' : '}',
        #     '(' : ')'
        # }
        # stack = []
        # for character in s:
        #     if character in ['(', '[', '{']:
        #         stack.append(character)
        #     else:
        #         if len(stack) == 0:
        #             return False
        #         topelement = stack.pop()
        #         if character == mapping[topelement]:
        #             continue
        #         else:
        #             return False
        # return len(stack) == 0
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

